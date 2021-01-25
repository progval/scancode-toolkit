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

# FIXME: the glob story is very weird!!!
examples_text = '''
Scancode command lines examples:

(Note for Windows: use '\\' back slash instead of '/' forward slash for paths.)

Scan a single file for copyrights. Print scan results to stdout as pretty JSON:

    scancode --copyright samples/zlib/zlib.h --json-pp -

Scan a single file for licenses, print verbose progress to stderr as each
file is scanned. Save scan to a JSON file:

    scancode --license --verbose samples/zlib/zlib.h --json licenses.json

Scan a directory explicitly for licenses and copyrights. Redirect JSON scan
results to a file:

    scancode --license --copyright samples/zlib/ --json - > scan.json

Scan a directory while ignoring a single file. Scan for license, copyright and
package manifests. Use four parallel processes.
Print scan results to stdout as pretty formatted JSON.

    scancode -lc --package --ignore README --processes 4 --json-pp - samples/

Scan a directory while ignoring all files with .txt extension.
Print scan results to stdout as pretty formatted JSON.
It is recommended to use quotes around glob patterns to prevent pattern
expansion by the shell:

    scancode --json-pp - --ignore "*.txt" samples/

Special characters supported in GLOB pattern:
- *       matches everything
- ?       matches any single character
- [seq]   matches any character in seq
- [!seq]  matches any character not in seq

For a literal match, wrap the meta-characters in brackets.
For example, '[?]' matches the character '?'.
For details on GLOB patterns see https://en.wikipedia.org/wiki/Glob_(programming).

Note: Glob patterns cannot be applied to path as strings.
For example, this will not ignore "samples/JGroups/licenses".

    scancode --json - --ignore "samples*licenses" samples/


Scan a directory while ignoring multiple files (or glob patterns).
Print the scan results to stdout as JSON:

    scancode --json - --ignore README --ignore "*.txt" samples/

Scan a directory for licenses and copyrights. Save scan results to an
HTML file:

    scancode --license --copyright --html scancode_result.html samples/zlib
'''

epilog_text = '''Examples (use --examples for more):

\b
Scan the 'samples' directory for licenses and copyrights.
Save scan results to the 'scancode_result.json' JSON file:

    scancode --license --copyright --json-pp scancode_result.json samples

\b
Scan the 'samples' directory for licenses and package manifests. Print scan
results on screen as pretty-formatted JSON (using the special '-' FILE to print
to on screen/to stdout):

    scancode --json-pp - --license --package  samples

Note: when you run scancode, a progress bar is displayed with a counter of the
number of files processed. Use --verbose to display file-by-file progress.
'''
