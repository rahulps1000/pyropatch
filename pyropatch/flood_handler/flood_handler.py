from ..utils import patch, patchable
import pyrogram
from pyrogram.errors import FloodWait
from asyncio import sleep


@patch(pyrogram.client.Client)
class Client():
    @patchable
    async def send_message(self, *args, **kwargs):
        try:
            return await self.old_send_message(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_message(*args, **kwargs)

    @patchable
    async def forward_messages(self, *args, **kwargs):
        try:
            return await self.old_forward_messages(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.forward_messages(*args, **kwargs)

    @patchable
    async def copy_message(self, *args, **kwargs):
        try:
            return await self.old_copy_message(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.copy_message(*args, **kwargs)

    @patchable
    async def copy_media_group(self, *args, **kwargs):
        try:
            return await self.old_copy_media_group(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.copy_media_group(*args, **kwargs)

    @patchable
    async def send_photo(self, *args, **kwargs):
        try:
            return await self.old_send_photo(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_photo(*args, **kwargs)

    @patchable
    async def send_audio(self, *args, **kwargs):
        try:
            return await self.old_send_audio(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_audio(*args, **kwargs)

    @patchable
    async def send_document(self, *args, **kwargs):
        try:
            return await self.old_send_document(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_document(*args, **kwargs)

    @patchable
    async def send_sticker(self, *args, **kwargs):
        try:
            return await self.old_send_sticker(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_sticker(*args, **kwargs)

    @patchable
    async def send_video(self, *args, **kwargs):
        try:
            return await self.old_send_video(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_video(*args, **kwargs)

    @patchable
    async def send_animation(self, *args, **kwargs):
        try:
            return await self.old_send_animation(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_animation(*args, **kwargs)

    @patchable
    async def send_voice(self, *args, **kwargs):
        try:
            return await self.old_send_voice(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_voice(*args, **kwargs)

    @patchable
    async def send_video_note(self, *args, **kwargs):
        try:
            return await self.old_send_video_note(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_video_note(*args, **kwargs)

    @patchable
    async def send_media_group(self, *args, **kwargs):
        try:
            return await self.old_send_media_group(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_media_group(*args, **kwargs)

    @patchable
    async def send_location(self, *args, **kwargs):
        try:
            return await self.old_send_location(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_location(*args, **kwargs)

    @patchable
    async def send_venue(self, *args, **kwargs):
        try:
            return await self.old_send_venue(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_venue(*args, **kwargs)

    @patchable
    async def send_contact(self, *args, **kwargs):
        try:
            return await self.old_send_contact(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_contact(*args, **kwargs)

    @patchable
    async def send_cached_media(self, *args, **kwargs):
        try:
            return await self.old_send_cached_media(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_cached_media(*args, **kwargs)

    @patchable
    async def send_reaction(self, *args, **kwargs):
        try:
            return await self.old_send_reaction(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_reaction(*args, **kwargs)

    @patchable
    async def edit_message_text(self, *args, **kwargs):
        try:
            return await self.old_edit_message_text(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_message_text(*args, **kwargs)

    @patchable
    async def edit_message_caption(self, *args, **kwargs):
        try:
            return await self.old_edit_message_caption(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_message_caption(*args, **kwargs)

    @patchable
    async def edit_message_media(self, *args, **kwargs):
        try:
            return await self.old_edit_message_media(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_message_media(*args, **kwargs)

    @patchable
    async def edit_message_reply_markup(self, *args, **kwargs):
        try:
            return await self.old_edit_message_reply_markup(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_message_reply_markup(*args, **kwargs)

    @patchable
    async def edit_inline_text(self, *args, **kwargs):
        try:
            return await self.old_edit_inline_text(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_inline_text(*args, **kwargs)

    @patchable
    async def edit_inline_caption(self, *args, **kwargs):
        try:
            return await self.old_edit_inline_caption(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_inline_caption(*args, **kwargs)

    @patchable
    async def edit_inline_media(self, *args, **kwargs):
        try:
            return await self.old_edit_inline_media(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_inline_media(*args, **kwargs)

    @patchable
    async def edit_inline_reply_markup(self, *args, **kwargs):
        try:
            return await self.old_edit_inline_reply_markup(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_inline_reply_markup(*args, **kwargs)

    @patchable
    async def send_chat_action(self, *args, **kwargs):
        try:
            return await self.old_send_chat_action(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_chat_action(*args, **kwargs)

    @patchable
    async def delete_messages(self, *args, **kwargs):
        try:
            return await self.old_delete_messages(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_messages(*args, **kwargs)

    @patchable
    async def get_messages(self, *args, **kwargs):
        try:
            return await self.old_get_messages(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_messages(*args, **kwargs)

    @patchable
    async def get_media_group(self, *args, **kwargs):
        try:
            return await self.old_get_media_group(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_media_group(*args, **kwargs)

    @patchable
    async def get_chat_history(self, *args, **kwargs):
        try:
            return await self.old_get_chat_history(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_history(*args, **kwargs)

    @patchable
    async def get_chat_history_count(self, *args, **kwargs):
        try:
            return await self.old_get_chat_history_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_history_count(*args, **kwargs)

    @patchable
    async def read_chat_history(self, *args, **kwargs):
        try:
            return await self.old_read_chat_history(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.read_chat_history(*args, **kwargs)

    @patchable
    async def send_poll(self, *args, **kwargs):
        try:
            return await self.old_send_poll(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_poll(*args, **kwargs)

    @patchable
    async def vote_poll(self, *args, **kwargs):
        try:
            return await self.old_vote_poll(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.vote_poll(*args, **kwargs)

    @patchable
    async def stop_poll(self, *args, **kwargs):
        try:
            return await self.old_stop_poll(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.stop_poll(*args, **kwargs)

    @patchable
    async def retract_vote(self, *args, **kwargs):
        try:
            return await self.old_retract_vote(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.retract_vote(*args, **kwargs)

    @patchable
    async def send_dice(self, *args, **kwargs):
        try:
            return await self.old_send_dice(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_dice(*args, **kwargs)

    @patchable
    async def search_messages(self, *args, **kwargs):
        try:
            return await self.old_search_messages(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.search_messages(*args, **kwargs)

    @patchable
    async def search_messages_count(self, *args, **kwargs):
        try:
            return await self.old_search_messages_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.search_messages_count(*args, **kwargs)

    @patchable
    async def search_global(self, *args, **kwargs):
        try:
            return await self.old_search_global(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.search_global(*args, **kwargs)

    @patchable
    async def search_global_count(self, *args, **kwargs):
        try:
            return await self.old_search_global_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.search_global_count(*args, **kwargs)

    @patchable
    async def download_media(self, *args, **kwargs):
        try:
            return await self.old_download_media(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.download_media(*args, **kwargs)

    @patchable
    async def stream_media(self, *args, **kwargs):
        try:
            return await self.old_stream_media(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.stream_media(*args, **kwargs)

    @patchable
    async def get_discussion_message(self, *args, **kwargs):
        try:
            return await self.old_get_discussion_message(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_discussion_message(*args, **kwargs)

    @patchable
    async def get_discussion_replies(self, *args, **kwargs):
        try:
            return await self.old_get_discussion_replies(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_discussion_replies(*args, **kwargs)

    @patchable
    async def get_discussion_replies_count(self, *args, **kwargs):
        try:
            return await self.old_get_discussion_replies_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_discussion_replies_count(*args, **kwargs)

    @patchable
    async def join_chat(self, *args, **kwargs):
        try:
            return await self.old_join_chat(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.join_chat(*args, **kwargs)

    @patchable
    async def leave_chat(self, *args, **kwargs):
        try:
            return await self.old_leave_chat(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.leave_chat(*args, **kwargs)

    @patchable
    async def ban_chat_member(self, *args, **kwargs):
        try:
            return await self.old_ban_chat_member(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.ban_chat_member(*args, **kwargs)

    @patchable
    async def unban_chat_member(self, *args, **kwargs):
        try:
            return await self.old_unban_chat_member(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.unban_chat_member(*args, **kwargs)

    @patchable
    async def restrict_chat_member(self, *args, **kwargs):
        try:
            return await self.old_restrict_chat_member(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.restrict_chat_member(*args, **kwargs)

    @patchable
    async def promote_chat_member(self, *args, **kwargs):
        try:
            return await self.old_promote_chat_member(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.promote_chat_member(*args, **kwargs)

    @patchable
    async def set_administrator_title(self, *args, **kwargs):
        try:
            return await self.old_set_administrator_title(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_administrator_title(*args, **kwargs)

    @patchable
    async def set_chat_photo(self, *args, **kwargs):
        try:
            return await self.old_set_chat_photo(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_photo(*args, **kwargs)

    @patchable
    async def delete_chat_photo(self, *args, **kwargs):
        try:
            return await self.old_delete_chat_photo(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_chat_photo(*args, **kwargs)

    @patchable
    async def set_chat_title(self, *args, **kwargs):
        try:
            return await self.old_set_chat_title(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_title(*args, **kwargs)

    @patchable
    async def set_chat_description(self, *args, **kwargs):
        try:
            return await self.old_set_chat_description(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_description(*args, **kwargs)

    @patchable
    async def set_chat_permissions(self, *args, **kwargs):
        try:
            return await self.old_set_chat_permissions(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_permissions(*args, **kwargs)

    @patchable
    async def pin_chat_message(self, *args, **kwargs):
        try:
            return await self.old_pin_chat_message(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.pin_chat_message(*args, **kwargs)

    @patchable
    async def unpin_chat_message(self, *args, **kwargs):
        try:
            return await self.old_unpin_chat_message(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.unpin_chat_message(*args, **kwargs)

    @patchable
    async def unpin_all_chat_messages(self, *args, **kwargs):
        try:
            return await self.old_unpin_all_chat_messages(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.unpin_all_chat_messages(*args, **kwargs)

    @patchable
    async def get_chat(self, *args, **kwargs):
        try:
            return await self.old_get_chat(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat(*args, **kwargs)

    @patchable
    async def get_chat_member(self, *args, **kwargs):
        try:
            return await self.old_get_chat_member(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_member(*args, **kwargs)

    @patchable
    async def get_chat_members(self, *args, **kwargs):
        try:
            return await self.old_get_chat_members(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_members(*args, **kwargs)

    @patchable
    async def get_chat_members_count(self, *args, **kwargs):
        try:
            return await self.old_get_chat_members_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_members_count(*args, **kwargs)

    @patchable
    async def get_dialogs(self, *args, **kwargs):
        try:
            return await self.old_get_dialogs(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_dialogs(*args, **kwargs)

    @patchable
    async def get_dialogs_count(self, *args, **kwargs):
        try:
            return await self.old_get_dialogs_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_dialogs_count(*args, **kwargs)

    @patchable
    async def set_chat_username(self, *args, **kwargs):
        try:
            return await self.old_set_chat_username(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_username(*args, **kwargs)

    @patchable
    async def get_nearby_chats(self, *args, **kwargs):
        try:
            return await self.old_get_nearby_chats(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_nearby_chats(*args, **kwargs)

    @patchable
    async def archive_chats(self, *args, **kwargs):
        try:
            return await self.old_archive_chats(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.archive_chats(*args, **kwargs)

    @patchable
    async def unarchive_chats(self, *args, **kwargs):
        try:
            return await self.old_unarchive_chats(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.unarchive_chats(*args, **kwargs)

    @patchable
    async def add_chat_members(self, *args, **kwargs):
        try:
            return await self.old_add_chat_members(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.add_chat_members(*args, **kwargs)

    @patchable
    async def create_channel(self, *args, **kwargs):
        try:
            return await self.old_create_channel(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.create_channel(*args, **kwargs)

    @patchable
    async def create_group(self, *args, **kwargs):
        try:
            return await self.old_create_group(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.create_group(*args, **kwargs)

    @patchable
    async def create_supergroup(self, *args, **kwargs):
        try:
            return await self.old_create_supergroup(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.create_supergroup(*args, **kwargs)

    @patchable
    async def delete_channel(self, *args, **kwargs):
        try:
            return await self.old_delete_channel(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_channel(*args, **kwargs)

    @patchable
    async def delete_supergroup(self, *args, **kwargs):
        try:
            return await self.old_delete_supergroup(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_supergroup(*args, **kwargs)

    @patchable
    async def delete_user_history(self, *args, **kwargs):
        try:
            return await self.old_delete_user_history(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_user_history(*args, **kwargs)

    @patchable
    async def set_slow_mode(self, *args, **kwargs):
        try:
            return await self.old_set_slow_mode(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_slow_mode(*args, **kwargs)

    @patchable
    async def mark_chat_unread(self, *args, **kwargs):
        try:
            return await self.old_mark_chat_unread(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.mark_chat_unread(*args, **kwargs)

    @patchable
    async def get_chat_event_log(self, *args, **kwargs):
        try:
            return await self.old_get_chat_event_log(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_event_log(*args, **kwargs)

    @patchable
    async def get_chat_online_count(self, *args, **kwargs):
        try:
            return await self.old_get_chat_online_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_online_count(*args, **kwargs)

    @patchable
    async def get_send_as_chats(self, *args, **kwargs):
        try:
            return await self.old_get_send_as_chats(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_send_as_chats(*args, **kwargs)

    @patchable
    async def set_send_as_chat(self, *args, **kwargs):
        try:
            return await self.old_set_send_as_chat(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_send_as_chat(*args, **kwargs)

    @patchable
    async def set_chat_protected_content(self, *args, **kwargs):
        try:
            return await self.old_set_chat_protected_content(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_protected_content(*args, **kwargs)

    @patchable
    async def get_me(self, *args, **kwargs):
        try:
            return await self.old_get_me(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_me(*args, **kwargs)

    @patchable
    async def get_users(self, *args, **kwargs):
        try:
            return await self.old_get_users(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_users(*args, **kwargs)

    @patchable
    async def get_chat_photos(self, *args, **kwargs):
        try:
            return await self.old_get_chat_photos(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_photos(*args, **kwargs)

    @patchable
    async def get_chat_photos_count(self, *args, **kwargs):
        try:
            return await self.old_get_chat_photos_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_photos_count(*args, **kwargs)

    @patchable
    async def set_profile_photo(self, *args, **kwargs):
        try:
            return await self.old_set_profile_photo(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_profile_photo(*args, **kwargs)

    @patchable
    async def delete_profile_photos(self, *args, **kwargs):
        try:
            return await self.old_delete_profile_photos(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_profile_photos(*args, **kwargs)

    @patchable
    async def set_username(self, *args, **kwargs):
        try:
            return await self.old_set_username(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_username(*args, **kwargs)

    @patchable
    async def update_profile(self, *args, **kwargs):
        try:
            return await self.old_update_profile(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.update_profile(*args, **kwargs)

    @patchable
    async def block_user(self, *args, **kwargs):
        try:
            return await self.old_block_user(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.block_user(*args, **kwargs)

    @patchable
    async def unblock_user(self, *args, **kwargs):
        try:
            return await self.old_unblock_user(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.unblock_user(*args, **kwargs)

    @patchable
    async def get_common_chats(self, *args, **kwargs):
        try:
            return await self.old_get_common_chats(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_common_chats(*args, **kwargs)

    @patchable
    async def get_chat_invite_link(self, *args, **kwargs):
        try:
            return await self.old_get_chat_invite_link(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_invite_link(*args, **kwargs)

    @patchable
    async def export_chat_invite_link(self, *args, **kwargs):
        try:
            return await self.old_export_chat_invite_link(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.export_chat_invite_link(*args, **kwargs)

    @patchable
    async def create_chat_invite_link(self, *args, **kwargs):
        try:
            return await self.old_create_chat_invite_link(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.create_chat_invite_link(*args, **kwargs)

    @patchable
    async def edit_chat_invite_link(self, *args, **kwargs):
        try:
            return await self.old_edit_chat_invite_link(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.edit_chat_invite_link(*args, **kwargs)

    @patchable
    async def revoke_chat_invite_link(self, *args, **kwargs):
        try:
            return await self.old_revoke_chat_invite_link(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.revoke_chat_invite_link(*args, **kwargs)

    @patchable
    async def delete_chat_invite_link(self, *args, **kwargs):
        try:
            return await self.old_delete_chat_invite_link(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_chat_invite_link(*args, **kwargs)

    @patchable
    async def get_chat_invite_link_joiners(self, *args, **kwargs):
        try:
            return await self.old_get_chat_invite_link_joiners(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_invite_link_joiners(*args, **kwargs)

    @patchable
    async def get_chat_invite_link_joiners_count(self, *args, **kwargs):
        try:
            return await self.old_get_chat_invite_link_joiners_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_invite_link_joiners_count(*args, **kwargs)

    @patchable
    async def get_chat_admin_invite_links(self, *args, **kwargs):
        try:
            return await self.old_get_chat_admin_invite_links(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_admin_invite_links(*args, **kwargs)

    @patchable
    async def get_chat_admin_invite_links_count(self, *args, **kwargs):
        try:
            return await self.old_get_chat_admin_invite_links_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_admin_invite_links_count(*args, **kwargs)

    @patchable
    async def get_chat_admins_with_invite_links(self, *args, **kwargs):
        try:
            return await self.old_get_chat_admins_with_invite_links(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_admins_with_invite_links(*args, **kwargs)

    @patchable
    async def get_chat_join_requests(self, *args, **kwargs):
        try:
            return await self.old_get_chat_join_requests(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_join_requests(*args, **kwargs)

    @patchable
    async def delete_chat_admin_invite_links(self, *args, **kwargs):
        try:
            return await self.old_delete_chat_admin_invite_links(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_chat_admin_invite_links(*args, **kwargs)

    @patchable
    async def approve_chat_join_request(self, *args, **kwargs):
        try:
            return await self.old_approve_chat_join_request(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.approve_chat_join_request(*args, **kwargs)

    @patchable
    async def approve_all_chat_join_requests(self, *args, **kwargs):
        try:
            return await self.old_approve_all_chat_join_requests(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.approve_all_chat_join_requests(*args, **kwargs)

    @patchable
    async def decline_chat_join_request(self, *args, **kwargs):
        try:
            return await self.old_decline_chat_join_request(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.decline_chat_join_request(*args, **kwargs)

    @patchable
    async def decline_all_chat_join_requests(self, *args, **kwargs):
        try:
            return await self.old_decline_all_chat_join_requests(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.decline_all_chat_join_requests(*args, **kwargs)

    @patchable
    async def add_contact(self, *args, **kwargs):
        try:
            return await self.old_add_contact(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.add_contact(*args, **kwargs)

    @patchable
    async def delete_contacts(self, *args, **kwargs):
        try:
            return await self.old_delete_contacts(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_contacts(*args, **kwargs)

    @patchable
    async def import_contacts(self, *args, **kwargs):
        try:
            return await self.old_import_contacts(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.import_contacts(*args, **kwargs)

    @patchable
    async def get_contacts(self, *args, **kwargs):
        try:
            return await self.old_get_contacts(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_contacts(*args, **kwargs)

    @patchable
    async def get_contacts_count(self, *args, **kwargs):
        try:
            return await self.old_get_contacts_count(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_contacts_count(*args, **kwargs)

    @patchable
    async def enable_cloud_password(self, *args, **kwargs):
        try:
            return await self.old_enable_cloud_password(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.enable_cloud_password(*args, **kwargs)

    @patchable
    async def change_cloud_password(self, *args, **kwargs):
        try:
            return await self.old_change_cloud_password(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.change_cloud_password(*args, **kwargs)

    @patchable
    async def remove_cloud_password(self, *args, **kwargs):
        try:
            return await self.old_remove_cloud_password(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.remove_cloud_password(*args, **kwargs)

    @patchable
    async def get_inline_bot_results(self, *args, **kwargs):
        try:
            return await self.old_get_inline_bot_results(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_inline_bot_results(*args, **kwargs)

    @patchable
    async def send_inline_bot_result(self, *args, **kwargs):
        try:
            return await self.old_send_inline_bot_result(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_inline_bot_result(*args, **kwargs)

    @patchable
    async def answer_callback_query(self, *args, **kwargs):
        try:
            return await self.old_answer_callback_query(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.answer_callback_query(*args, **kwargs)

    @patchable
    async def answer_inline_query(self, *args, **kwargs):
        try:
            return await self.old_answer_inline_query(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.answer_inline_query(*args, **kwargs)

    @patchable
    async def request_callback_answer(self, *args, **kwargs):
        try:
            return await self.old_request_callback_answer(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.request_callback_answer(*args, **kwargs)

    @patchable
    async def send_game(self, *args, **kwargs):
        try:
            return await self.old_send_game(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_game(*args, **kwargs)

    @patchable
    async def set_game_score(self, *args, **kwargs):
        try:
            return await self.old_set_game_score(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_game_score(*args, **kwargs)

    @patchable
    async def get_game_high_scores(self, *args, **kwargs):
        try:
            return await self.old_get_game_high_scores(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_game_high_scores(*args, **kwargs)

    @patchable
    async def set_bot_commands(self, *args, **kwargs):
        try:
            return await self.old_set_bot_commands(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_bot_commands(*args, **kwargs)

    @patchable
    async def get_bot_commands(self, *args, **kwargs):
        try:
            return await self.old_get_bot_commands(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_bot_commands(*args, **kwargs)

    @patchable
    async def delete_bot_commands(self, *args, **kwargs):
        try:
            return await self.old_delete_bot_commands(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.delete_bot_commands(*args, **kwargs)

    @patchable
    async def set_bot_default_privileges(self, *args, **kwargs):
        try:
            return await self.old_set_bot_default_privileges(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_bot_default_privileges(*args, **kwargs)

    @patchable
    async def get_bot_default_privileges(self, *args, **kwargs):
        try:
            return await self.old_get_bot_default_privileges(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_bot_default_privileges(*args, **kwargs)

    @patchable
    async def set_chat_menu_button(self, *args, **kwargs):
        try:
            return await self.old_set_chat_menu_button(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.set_chat_menu_button(*args, **kwargs)

    @patchable
    async def get_chat_menu_button(self, *args, **kwargs):
        try:
            return await self.old_get_chat_menu_button(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_chat_menu_button(*args, **kwargs)

    @patchable
    async def answer_web_app_query(self, *args, **kwargs):
        try:
            return await self.old_answer_web_app_query(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.answer_web_app_query(*args, **kwargs)

    @patchable
    async def connect(self, *args, **kwargs):
        try:
            return await self.old_connect(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.connect(*args, **kwargs)

    @patchable
    async def disconnect(self, *args, **kwargs):
        try:
            return await self.old_disconnect(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.disconnect(*args, **kwargs)

    @patchable
    async def initialize(self, *args, **kwargs):
        try:
            return await self.old_initialize(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.initialize(*args, **kwargs)

    @patchable
    async def terminate(self, *args, **kwargs):
        try:
            return await self.old_terminate(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.terminate(*args, **kwargs)

    @patchable
    async def send_code(self, *args, **kwargs):
        try:
            return await self.old_send_code(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_code(*args, **kwargs)

    @patchable
    async def resend_code(self, *args, **kwargs):
        try:
            return await self.old_resend_code(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.resend_code(*args, **kwargs)

    @patchable
    async def sign_in(self, *args, **kwargs):
        try:
            return await self.old_sign_in(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.sign_in(*args, **kwargs)

    @patchable
    async def sign_in_bot(self, *args, **kwargs):
        try:
            return await self.old_sign_in_bot(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.sign_in_bot(*args, **kwargs)

    @patchable
    async def sign_up(self, *args, **kwargs):
        try:
            return await self.old_sign_up(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.sign_up(*args, **kwargs)

    @patchable
    async def get_password_hint(self, *args, **kwargs):
        try:
            return await self.old_get_password_hint(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.get_password_hint(*args, **kwargs)

    @patchable
    async def check_password(self, *args, **kwargs):
        try:
            return await self.old_check_password(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.check_password(*args, **kwargs)

    @patchable
    async def send_recovery_code(self, *args, **kwargs):
        try:
            return await self.old_send_recovery_code(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.send_recovery_code(*args, **kwargs)

    @patchable
    async def recover_password(self, *args, **kwargs):
        try:
            return await self.old_recover_password(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.recover_password(*args, **kwargs)

    @patchable
    async def accept_terms_of_service(self, *args, **kwargs):
        try:
            return await self.old_accept_terms_of_service(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.accept_terms_of_service(*args, **kwargs)

    @patchable
    async def log_out(self, *args, **kwargs):
        try:
            return await self.old_log_out(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.log_out(*args, **kwargs)

    @patchable
    async def invoke(self, *args, **kwargs):
        try:
            return await self.old_invoke(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.invoke(*args, **kwargs)

    @patchable
    async def resolve_peer(self, *args, **kwargs):
        try:
            return await self.old_resolve_peer(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.resolve_peer(*args, **kwargs)

    @patchable
    async def save_file(self, *args, **kwargs):
        try:
            return await self.old_save_file(*args, **kwargs)
        except FloodWait as e:
            await sleep(e.value)
            return await self.save_file(*args, **kwargs)
