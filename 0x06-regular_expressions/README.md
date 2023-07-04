# 0x06-regular_expressions
Oniguruma is a powerful ruby library by default that supports a wide range of regular expression features.

## Matching Characters:

* . matches any character except newline.
* [abc] matches any single character in the set a, b, or c.
* [^abc] matches any single character except a, b, or c.
* \w matches any word character (alphanumeric or underscore).
* \W matches any non-word character.
* \d matches any digit character.
* \D matches any non-digit character.
* \s matches any whitespace character.
* \S matches any non-whitespace character.
* \b matches a word boundary.

## Repetition:

* *matches zero or more occurrences.
* + matches one or more occurrences.
* ? matches zero or one occurrence.
* {n} matches exactly n occurrences.
* {n,} matches n or more occurrences.
* {n,m} matches between n and m occurrences (inclusive).

## Anchors:

* ^ matches the start of a line/string.
* $ matches the end of a line/string.
* \A matches the start of a string.
* \z matches the end of a string.

## Groups and Capturing:

* (...) creates a capturing group.
* (?:...) creates a non-capturing group.

## Alternation:

| allows for multiple alternatives.

## Escaping:

Use \ to escape special characters like . or * if you want to match them literally.

