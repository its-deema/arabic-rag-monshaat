# Eval set

One JSON object per line in `questions.jsonl`:

| field | meaning |
| --- | --- |
| `id` | `q001`, `q002`, ... |
| `question` | the question as a user would type it |
| `style` | `msa` or `saudi` (dialect) |
| `answerable` | `false` if the docs do not contain the answer |
| `sources` | list of `{"doc": file name, "page": n}` holding the answer |
| `answer` | short reference answer (empty when not answerable) |

Target for week 1: 50 to 100 questions, about 20% dialect and 10 to 15% unanswerable.
The example line below is a format sample only; replace it with real questions.
