# SPDX-FileCopyrightText: Copyright (c) 2021 Art Galkin <ortemeo@gmail.com>
# SPDX-FileCopyrightText: Copyright (c) 2015 Jean-Ralph Aviles
# SPDX-License-Identifier: MIT

import unittest
from typing import List

from commie import iter_comments_shell, Comment


def commentsToList(code:str) -> List[Comment]:
  return list(iter_comments_shell(code))

class ShellParserTest(unittest.TestCase):

  def testComment(self):
    code = '# comment'
    comments = commentsToList(code)
    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].code_span.extract(code), '# comment')
    self.assertEqual(comments[0].text_span.extract(code), " comment")
    self.assertEqual(comments[0].multiline, False)

  def testEscapedComment(self):
    code = r'\# not a comment'
    comments = commentsToList(code)
    self.assertEqual(comments, [])

  def testCommentInSingleQuotedString(self):
    code = "'this is # not a comment'"
    comments = commentsToList(code)
    self.assertEqual(comments, [])

  def testCommentInDoubleQuotedString(self):
    code = '"this is # not a comment"'
    comments = commentsToList(code)
    self.assertEqual(comments, [])

  def testNestedStringSingleOutside(self):
    code = "'this is \"# not a comment\"'"
    comments = commentsToList(code)
    self.assertEqual(comments, [])

  def testNestedStringDoubleOutside(self):
    code = '"this is \'# not a comment\'"'
    comments = commentsToList(code)
    self.assertEqual(comments, [])

  def testEscapedSingleQuote(self):
    code = "\\'# this is a comment"
    comments = commentsToList(code)
    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].code_span.extract(code), "# this is a comment")
    self.assertEqual(comments[0].text_span.extract(code), " this is a comment")
    self.assertEqual(comments[0].multiline, False)

  def testEscapedDoubleQuote(self):
    code = '\\"# this is another comment'
    comments = commentsToList(code)

    self.assertEqual(len(comments), 1)

    self.assertEqual(comments[0].code_span.extract(code), "# this is another comment")
    self.assertEqual(comments[0].text_span.extract(code), " this is another comment")
    self.assertEqual(comments[0].multiline, False)

