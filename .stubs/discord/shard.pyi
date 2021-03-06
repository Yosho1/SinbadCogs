import asyncio
import aiohttp

from .client import Client
from .guild import Guild
from .activity import Activity, Game, Streaming, Spotify
from .enums import Status

from typing import Any, List, Tuple, Optional, Union, overload

class Shard:
    @property
    def id(self) -> int: ...
    def is_pending(self) -> bool: ...
    def complete_pending_reads(self) -> None: ...
    def launch_pending_reads(self) -> None: ...
    def wait(self) -> Optional[asyncio.Future]: ...
    async def poll(self) -> None: ...
    def get_future(self) -> asyncio.Future: ...

class AutoShardedClient(Client):
    shard_ids: Optional[Union[List[int], Tuple[int]]]
    @overload
    def __init__(
        self,
        *args: Any,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        shard_ids: Union[List[int], Tuple[int]] = ...,
        shard_count: int = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        max_messages: Optional[int] = ...,
        fetch_offline_members: bool = ...,
        status: Optional[Status] = ...,
        activity: Optional[Union[Activity, Game, Streaming]] = ...,
        heartbeat_timeout: float = ...,
        **kwargs: Any,
    ) -> None: ...
    @overload
    def __init__(
        self,
        *args: Any,
        loop: Optional[asyncio.AbstractEventLoop] = ...,
        shard_count: Optional[int] = ...,
        connector: aiohttp.BaseConnector = ...,
        proxy: Optional[str] = ...,
        proxy_auth: Optional[aiohttp.BasicAuth] = ...,
        max_messages: Optional[int] = ...,
        fetch_offline_members: bool = ...,
        status: Optional[Status] = ...,
        activity: Optional[Union[Activity, Game, Streaming]] = ...,
        heartbeat_timeout: float = ...,
        **kwargs: Any,
    ) -> None: ...
    @property
    def latency(self) -> float: ...
    @property
    def latencies(self) -> List[Tuple[int, float]]: ...
    async def request_offline_members(self, *guilds: Guild) -> None: ...
    async def launch_shard(self, gateway: str, shard_id: int) -> None: ...
    async def launch_shards(self) -> None: ...
    async def close(self) -> None: ...
    async def change_presence(
        self,
        *,
        activity: Optional[Union[Activity, Game, Streaming, Spotify]] = ...,
        status: Optional[Status] = ...,
        afk: bool = ...,
        shard_id: Optional[int] = ...,
    ) -> None: ...
