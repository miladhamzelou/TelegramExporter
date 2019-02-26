"""File generated by TLObjects' generator. All changes will be ERASED"""
from ...tl.tlobject import TLObject
from ...tl.tlobject import TLRequest
from typing import Optional, List, Union, TYPE_CHECKING
import os
import struct
if TYPE_CHECKING:
    from ...tl.types import TypeInputStickerSetItem, TypeInputStickerSet, TypeInputUser, TypeInputDocument



class AddStickerToSetRequest(TLRequest):
    CONSTRUCTOR_ID = 0x8653febe
    SUBCLASS_OF_ID = 0x9b704a5a

    def __init__(self, stickerset, sticker):
        """
        :param TypeInputStickerSet stickerset:
        :param TypeInputStickerSetItem sticker:

        :returns messages.StickerSet: Instance of StickerSet.
        """
        self.stickerset = stickerset  # type: TypeInputStickerSet
        self.sticker = sticker  # type: TypeInputStickerSetItem

    def to_dict(self):
        return {
            '_': 'AddStickerToSetRequest',
            'stickerset': self.stickerset.to_dict() if isinstance(self.stickerset, TLObject) else self.stickerset,
            'sticker': self.sticker.to_dict() if isinstance(self.sticker, TLObject) else self.sticker
        }

    def __bytes__(self):
        return b''.join((
            b'\xbe\xfeS\x86',
            bytes(self.stickerset),
            bytes(self.sticker),
        ))

    @classmethod
    def from_reader(cls, reader):
        _stickerset = reader.tgread_object()
        _sticker = reader.tgread_object()
        return cls(stickerset=_stickerset, sticker=_sticker)


class ChangeStickerPositionRequest(TLRequest):
    CONSTRUCTOR_ID = 0xffb6d4ca
    SUBCLASS_OF_ID = 0x9b704a5a

    def __init__(self, sticker, position):
        """
        :param TypeInputDocument sticker:
        :param int position:

        :returns messages.StickerSet: Instance of StickerSet.
        """
        self.sticker = sticker  # type: TypeInputDocument
        self.position = position  # type: int

    async def resolve(self, client, utils):
        self.sticker = utils.get_input_document(self.sticker)

    def to_dict(self):
        return {
            '_': 'ChangeStickerPositionRequest',
            'sticker': self.sticker.to_dict() if isinstance(self.sticker, TLObject) else self.sticker,
            'position': self.position
        }

    def __bytes__(self):
        return b''.join((
            b'\xca\xd4\xb6\xff',
            bytes(self.sticker),
            struct.pack('<i', self.position),
        ))

    @classmethod
    def from_reader(cls, reader):
        _sticker = reader.tgread_object()
        _position = reader.read_int()
        return cls(sticker=_sticker, position=_position)


class CreateStickerSetRequest(TLRequest):
    CONSTRUCTOR_ID = 0x9bd86e6a
    SUBCLASS_OF_ID = 0x9b704a5a

    def __init__(self, user_id, title, short_name, stickers, masks=None):
        """
        :param TypeInputUser user_id:
        :param str title:
        :param str short_name:
        :param List[TypeInputStickerSetItem] stickers:
        :param Optional[bool] masks:

        :returns messages.StickerSet: Instance of StickerSet.
        """
        self.user_id = user_id  # type: TypeInputUser
        self.title = title  # type: str
        self.short_name = short_name  # type: str
        self.stickers = stickers  # type: List[TypeInputStickerSetItem]
        self.masks = masks  # type: Optional[bool]

    async def resolve(self, client, utils):
        self.user_id = utils.get_input_user(await client.get_input_entity(self.user_id))

    def to_dict(self):
        return {
            '_': 'CreateStickerSetRequest',
            'user_id': self.user_id.to_dict() if isinstance(self.user_id, TLObject) else self.user_id,
            'title': self.title,
            'short_name': self.short_name,
            'stickers': [] if self.stickers is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.stickers],
            'masks': self.masks
        }

    def __bytes__(self):
        return b''.join((
            b'jn\xd8\x9b',
            struct.pack('<I', (0 if self.masks is None or self.masks is False else 1)),
            bytes(self.user_id),
            self.serialize_bytes(self.title),
            self.serialize_bytes(self.short_name),
            b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.stickers)),b''.join(bytes(x) for x in self.stickers),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _masks = bool(flags & 1)
        _user_id = reader.tgread_object()
        _title = reader.tgread_string()
        _short_name = reader.tgread_string()
        reader.read_int()
        _stickers = []
        for _ in range(reader.read_int()):
            _x = reader.tgread_object()
            _stickers.append(_x)

        return cls(user_id=_user_id, title=_title, short_name=_short_name, stickers=_stickers, masks=_masks)


class RemoveStickerFromSetRequest(TLRequest):
    CONSTRUCTOR_ID = 0xf7760f51
    SUBCLASS_OF_ID = 0x9b704a5a

    def __init__(self, sticker):
        """
        :param TypeInputDocument sticker:

        :returns messages.StickerSet: Instance of StickerSet.
        """
        self.sticker = sticker  # type: TypeInputDocument

    async def resolve(self, client, utils):
        self.sticker = utils.get_input_document(self.sticker)

    def to_dict(self):
        return {
            '_': 'RemoveStickerFromSetRequest',
            'sticker': self.sticker.to_dict() if isinstance(self.sticker, TLObject) else self.sticker
        }

    def __bytes__(self):
        return b''.join((
            b'Q\x0fv\xf7',
            bytes(self.sticker),
        ))

    @classmethod
    def from_reader(cls, reader):
        _sticker = reader.tgread_object()
        return cls(sticker=_sticker)

