import re

from commie.common import Comment, Span


def matchGroupToComment(match:re.Match, groupName:str, multiline:bool) -> Comment:

  fullSpan = match.span()

  fullText = match.group(0)
  innerText = match.group(groupName)
  textStart = fullText.index(innerText)
  assert textStart>=0

  return Comment(
    text_span=Span(fullSpan[0]+textStart, fullSpan[0]+textStart+len(innerText)),
    markup_span=Span(fullSpan[0], fullSpan[1]),
    multiline=multiline)