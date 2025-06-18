from src.core.controllers.platform import PlatformController
from src.core.models.platform import PlatformModel
from src.core.views.platform import PlatformView
from src.core.utils.abstract_factory import AbstractMVCFactory


class PlatformFactory(AbstractMVCFactory[PlatformModel, PlatformView, PlatformController]):
    def create_model(x: int, y: int):
        return PlatformModel(x, y)

    def create_view():
        return PlatformView()

    def create_controller(model, view):
        return PlatformController(model, view)
    
    def create_mvc_component(x: int, y: int):
        model = PlatformFactory.create_model(x, y)
        view = PlatformFactory.create_view()
        controller = PlatformFactory.create_controller(model, view)
        return controller