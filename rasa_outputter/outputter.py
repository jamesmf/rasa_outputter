import typing
from typing import Any, Optional, Text, Dict, List, Type

from rasa.nlu.components import Component
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.training_data import Message, TrainingData

if typing.TYPE_CHECKING:
    from rasa.nlu.model import Metadata


class Outputter(Component):
    """
    A component that is used to add any internal message properties to
    the message's output. Useful if you want to make use of the feature
    vectors, return how text was tokenized, etc
    """

    defaults = {"properties_to_add": []}

    language_list = None

    def __init__(self, component_config: Optional[Dict[Text, Any]] = None) -> None:
        super().__init__(component_config)
        self.properties_to_add = component_config["properties_to_add"]

    def train(
        self,
        training_data: TrainingData,
        config: Optional[RasaNLUModelConfig] = None,
        **kwargs: Any,
    ) -> None:
        """Train this component.

        This is the components chance to train itself provided
        with the training data. The component can rely on
        any context attribute to be present, that gets created
        by a call to :meth:`components.Component.pipeline_init`
        of ANY component and
        on any context attributes created by a call to
        :meth:`components.Component.train`
        of components previous to this one."""
        pass

    def process(self, message: Message, **kwargs: Any) -> None:
        """
        This is where we care about adding to the message, as this
        is where we can see it. Take each attribute in `properties_to_add`
        and add it to the output
        """
        print(message)
        print(message.as_dict())
        for prop in self.properties_to_add:
            print(prop)
            prop_val = message.get(prop)
            message.set(prop, prop_val, add_to_output=True)

    def persist(self, file_name: Text, model_dir: Text) -> Optional[Dict[Text, Any]]:
        """Persist this component to disk for future loading."""

        pass

    @classmethod
    def load(
        cls,
        meta: Dict[Text, Any],
        model_dir: Optional[Text] = None,
        model_metadata: Optional["Metadata"] = None,
        cached_component: Optional["Component"] = None,
        **kwargs: Any,
    ) -> "Component":
        """Load this component from file."""

        if cached_component:
            return cached_component
        else:
            return cls(meta)
