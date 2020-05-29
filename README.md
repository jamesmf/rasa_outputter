# rasa_outputter
Extra component to output internals of your rasa pipeline


## Usage

To get the outputs you want, add an `Outputter` to your pipeline at the end

```
- name: rasa_outputter.outputter.Outputter
  properties_to_add: ["tokens", "text_sparse_features"]
```

Now the `tokens` and `text_sparse_features` properties will be present on the response from `Interpreter.parse()`


```
from rasa.nlu.model import Interpreter
model = Interpreter.load("nlu")

response = model.parse("hello friend!")
print([tok.text for tok in response["tokens"]])

print(response["text_sparse_features"].shape)
```

For a `WhitespaceTokenizer` and `CountVectorsFeaturizer` this might return `['hello', 'friend', '__CLS__']` and `(3, 561)` with the basic data from `rasa init`.
