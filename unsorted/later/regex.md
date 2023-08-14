---
published: false
---

## Find ``` replace with <code>

> ```
> <code>

### Replace quotes with <br> in quoted section
1: First Line
\n> <code>\n> (.*)
\n<code>$1<br>
2: Second lines
\n(<code>.*)\n> (.*)
\n$1<br>$2

### Close </code>

1:
<br><br><code>
</code>
2:
<br><code>
</code>

## Find Quote and replace with linebreak

\n> (.*)\n>
\n$1<br>

\n\n(.*)\n  > (.*)
\n\n$1<br>

## Nested Quotes

(\* .*)\n  > (.*)\n  >
\n\n$1<br>$2

## Format row with trailing author\other info

\* \[(.*)\]\((.*)\) (.*)\n\n(.*)
$1\t$4\t$2\t$3

###  Same with different space

\* \[(.*)\]\((.*)\) (.*)\n\n(.*)
$1\t$4\t$2\t$3

### Same with leading note

\* (.*)\[(.*)\]\((.*)\) (.*)\n\n(.*)
$1\t$4\t$2\t$3\$5