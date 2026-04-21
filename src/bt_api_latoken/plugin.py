from __future__ import annotations

from typing import Any

from bt_api_base.plugins.protocol import PluginInfo

from bt_api_latoken import __version__
from bt_api_latoken.registry_registration import register_latoken


def get_plugin_info() -> PluginInfo:
    return PluginInfo(
        name="bt_api_latoken",
        version=__version__,
        core_requires=">=0.15,<1.0",
        supported_exchanges=("LATOKEN___SPOT",),
        supported_asset_types=("SPOT",),
        plugin_module="bt_api_latoken.plugin",
    )


def register_plugin(registry: Any, runtime_factory: Any) -> PluginInfo:
    del runtime_factory
    register_latoken(registry)
    return get_plugin_info()
