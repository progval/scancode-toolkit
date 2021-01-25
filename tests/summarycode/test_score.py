#
# Copyright (c) nexB Inc. and others. All rights reserved.
# SPDX-License-Identifier: Apache-2.0 AND CC-BY-4.0
#
# Visit https://aboutcode.org and https://github.com/nexB/scancode-toolkit for
# support and download. ScanCode is a trademark of nexB Inc.
#
# The ScanCode software is licensed under the Apache License version 2.0.
# The ScanCode open data is licensed under CC-BY-4.0.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import io
import os

import click
import pytest

from commoncode.testcase import FileDrivenTesting
from commoncode.text import python_safe_name
from scancode.cli_test_utils import check_json_scan
from scancode.cli_test_utils import run_scan_click


pytestmark = pytest.mark.scanslow


"""
Data-driven Score test utilities.
"""


test_env = FileDrivenTesting()
test_env.test_data_dir = os.path.join(os.path.dirname(__file__), 'data')


def make_test_function(test_name, test_dir, expected_file, regen=False):
    """
    Build and return a test function closing on tests arguments and the function
    name. Create only a single function for multiple tests (e.g. copyrights and
    holders together).
    """

    def closure_test_function(*args, **kwargs):
        result_file = test_env.get_temp_file('json')
        args = ['--license',
                '--copyright',
                '--info',
                '--classify',
                '--license-clarity-score',
                test_dir, '--json', result_file]
        run_scan_click(args)
        run_scan_click(args)
        check_json_scan(
            test_env.get_test_loc(expected_file),
            result_file,
            remove_file_date=True,
            regen=regen)

    test_name = 'test_license_clarity_score_%(test_name)s' % locals()
    test_name = python_safe_name(test_name)
    if isinstance(test_name, bytes):
        test_name = test_name.decode('utf-8')

    closure_test_function.__name__ = test_name

    return closure_test_function, test_name


def build_tests(test_base_dir, clazz, regen=False):
    """
    Dynamically build test methods from a sequence of CopyrightTest and attach
    these method to the clazz test class.
    """
    test_dirs = test_env.get_test_loc(test_base_dir)
    for td in os.listdir(test_dirs):
        td_loc = os.path.join(test_dirs, td)
        if not os.path.isdir(td_loc):
            continue
        expected_file_loc = td_loc.rstrip('/\\') + '-expected.json'

        if regen and not os.path.exists(expected_file_loc):
            with io.open(expected_file_loc, 'w') as o:
                o.write(u'')

        method, name = make_test_function(
            test_name=td,
            test_dir=td_loc,
            expected_file=expected_file_loc,
            regen=regen)

        # attach that method to our test class
        setattr(clazz, name, method)


class TestLicenseScore(FileDrivenTesting):
    # test functions are attached to this class at module import time
    pass


build_tests(test_base_dir='score', clazz=TestLicenseScore, regen=False)
