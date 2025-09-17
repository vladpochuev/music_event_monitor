import unittest

from main import extract_first_package_block


class TestMain(unittest.TestCase):
    def test_extract_first_package_block_youtube(self):
        output = """
        MEDIA SESSION SERVICE (dumpsys media_session)

        5 sessions listeners.
        Global priority session is com.android.server.telecom/HeadsetMediaButton (userId=0)
          HeadsetMediaButton com.android.server.telecom/HeadsetMediaButton (userId=0)
            ownerPid=1539, ownerUid=1000, userId=0
            package=com.android.server.telecom
            launchIntent=null
            mediaButtonReceiver=null
            active=false
            flags=65537
            rating type=0
            controllers: 0
            state=null
            audioAttrs=AudioAttributes: usage=USAGE_VOICE_COMMUNICATION content=CONTENT_TYPE_SPEECH flags=0x800 tags= bundle=null
            volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
            metadata: null
            queueTitle=null, size=0
        User Records:
        Record for full_user=0
          Volume key long-press listener: null
          Volume key long-press listener package: 
          Media key listener: null
          Media key listener package: 
          OnMediaKeyEventDispatchedListener: added 0 listener(s)
          OnMediaKeyEventSessionChangedListener: added 0 listener(s)
          Last MediaButtonReceiver: MBR {pi=PendingIntent{a654f06: PendingIntentRecord{abf9368 com.google.android.apps.youtube.music broadcastIntent}}, componentName=ComponentInfo{com.google.android.apps.youtube.music/androidx.media.session.MediaButtonReceiver}, type=1, pkg=com.google.android.apps.youtube.music}
          Media button session is com.google.android.apps.youtube.music/YouTube playerlib (userId=0)
          Sessions Stack - have 1 sessions:
            YouTube playerlib com.google.android.apps.youtube.music/YouTube playerlib (userId=0)
              ownerPid=22377, ownerUid=10239, userId=0
              package=com.google.android.apps.youtube.music
              launchIntent=PendingIntent{fdaa9c7: PendingIntentRecord{2ec1c26 com.google.android.apps.youtube.music startActivity}}
              mediaButtonReceiver=MBR {pi=PendingIntent{a654f06: PendingIntentRecord{abf9368 com.google.android.apps.youtube.music broadcastIntent}}, componentName=ComponentInfo{com.google.android.apps.youtube.music/androidx.media.session.MediaButtonReceiver}, type=1, pkg=com.google.android.apps.youtube.music}
              active=true
              flags=3
              rating type=2
              controllers: 5
              state=PlaybackState {state=PLAYING(3), position=0, buffered position=0, speed=1.0, updated=671704199, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232771, mExtras=null, Action:mName='Like, mIcon=2131233494, mExtras=null, Action:mName='Repeat off, mIcon=2131232684, mExtras=null, Action:mName='Dislike, mIcon=2131233487, mExtras=null], active item id=26, error=null}
              audioAttrs=AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_UNKNOWN flags=0x800 tags= bundle=null
              volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
              metadata: size=7, description=Living in the Past (2001 Remaster), Jethro Tull, Jethro Tull
              queueTitle=Up next, size=25
        Audio playback (lastly played comes first)
          uid=10239 packages=com.google.android.apps.youtube.music 
        Media session config:
          media_button_receiver_fgs_allowlist_duration_ms: [cur: 10000, def: 10000]
          media_session_calback_fgs_allowlist_duration_ms: [cur: 10000, def: 10000]
          media_session_callback_fgs_while_in_use_temp_allow_duration_ms: [cur: 10000, def: 10000]
        """

        expected = """ownerPid=22377, ownerUid=10239, userId=0
package=com.google.android.apps.youtube.music
launchIntent=PendingIntent{fdaa9c7: PendingIntentRecord{2ec1c26 com.google.android.apps.youtube.music startActivity}}
mediaButtonReceiver=MBR {pi=PendingIntent{a654f06: PendingIntentRecord{abf9368 com.google.android.apps.youtube.music broadcastIntent}}, componentName=ComponentInfo{com.google.android.apps.youtube.music/androidx.media.session.MediaButtonReceiver}, type=1, pkg=com.google.android.apps.youtube.music}
active=true
flags=3
rating type=2
controllers: 5
state=PlaybackState {state=PLAYING(3), position=0, buffered position=0, speed=1.0, updated=671704199, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232771, mExtras=null, Action:mName='Like, mIcon=2131233494, mExtras=null, Action:mName='Repeat off, mIcon=2131232684, mExtras=null, Action:mName='Dislike, mIcon=2131233487, mExtras=null], active item id=26, error=null}
audioAttrs=AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_UNKNOWN flags=0x800 tags= bundle=null
volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
metadata: size=7, description=Living in the Past (2001 Remaster), Jethro Tull, Jethro Tull
queueTitle=Up next, size=25"""
        self.assertEqual(extract_first_package_block(output), expected)

    def test_extract_first_package_block_beatport(self):
        output = """
        MEDIA SESSION SERVICE (dumpsys media_session)
        
        5 sessions listeners.
        Global priority session is com.android.server.telecom/HeadsetMediaButton (userId=0)
          HeadsetMediaButton com.android.server.telecom/HeadsetMediaButton (userId=0)
            ownerPid=1539, ownerUid=1000, userId=0
            package=com.android.server.telecom
            launchIntent=null
            mediaButtonReceiver=null
            active=false
            flags=65537
            rating type=0
            controllers: 0
            state=null
            audioAttrs=AudioAttributes: usage=USAGE_VOICE_COMMUNICATION content=CONTENT_TYPE_SPEECH flags=0x800 tags= bundle=null
            volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
            metadata: null
            queueTitle=null, size=0
        User Records:
        Record for full_user=0
          Volume key long-press listener: null
          Volume key long-press listener package: 
          Media key listener: null
          Media key listener package: 
          OnMediaKeyEventDispatchedListener: added 0 listener(s)
          OnMediaKeyEventSessionChangedListener: added 0 listener(s)
          Last MediaButtonReceiver: MBR {pi=null, componentName=ComponentInfo{com.beatport.mobile/com.beatport.mobile.features.streaming.util.CustomMediaReceiver}, type=1, pkg=com.beatport.mobile}
          Media button session is com.beatport.mobile/androidx.media3.session.id. (userId=0)
          Sessions Stack - have 2 sessions:
            androidx.media3.session.id. com.beatport.mobile/androidx.media3.session.id. (userId=0)
              ownerPid=31847, ownerUid=10461, userId=0
              package=com.beatport.mobile
              launchIntent=PendingIntent{6654657: PendingIntentRecord{e6a465d com.beatport.mobile startActivity (allowlist: 8019200:+30s0ms/0/NOTIFICATION_SERVICE/NotificationManagerService)}}
              mediaButtonReceiver=MBR {pi=null, componentName=ComponentInfo{com.beatport.mobile/com.beatport.mobile.features.streaming.util.CustomMediaReceiver}, type=1, pkg=com.beatport.mobile}
              active=true
              flags=7
              rating type=0
              controllers: 5
              state=PlaybackState {state=PLAYING(3), position=2910, buffered position=87275, speed=1.0, updated=671962059, actions=7340031, custom actions=[], active item id=0, error=null}
              audioAttrs=AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x800 tags= bundle=null
              volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
              metadata: size=24, description=We Can Feel It (Original Mix), Dominik Marz, Radial Gaze, Duro
              queueTitle=null, size=3
            YouTube playerlib com.google.android.apps.youtube.music/YouTube playerlib (userId=0)
              ownerPid=22377, ownerUid=10239, userId=0
              package=com.google.android.apps.youtube.music
              launchIntent=PendingIntent{fdaa9c7: PendingIntentRecord{2ec1c26 com.google.android.apps.youtube.music startActivity}}
              mediaButtonReceiver=MBR {pi=PendingIntent{a654f06: PendingIntentRecord{abf9368 com.google.android.apps.youtube.music broadcastIntent}}, componentName=ComponentInfo{com.google.android.apps.youtube.music/androidx.media.session.MediaButtonReceiver}, type=1, pkg=com.google.android.apps.youtube.music}
              active=true
              flags=3
              rating type=2
              controllers: 4
              state=PlaybackState {state=PAUSED(2), position=24426, buffered position=0, speed=1.0, updated=671925843, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232771, mExtras=null, Action:mName='Like, mIcon=2131233494, mExtras=null, Action:mName='Repeat off, mIcon=2131232684, mExtras=null, Action:mName='Dislike, mIcon=2131233487, mExtras=null], active item id=26, error=null}
              audioAttrs=AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_UNKNOWN flags=0x800 tags= bundle=null
              volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
              metadata: size=9, description=Living in the Past (2001 Remaster), Jethro Tull, The Very Best of Jethro Tull
              queueTitle=Up next, size=25
        Audio playback (lastly played comes first)
          uid=10461 packages=com.beatport.mobile 
        Media session config:
          media_button_receiver_fgs_allowlist_duration_ms: [cur: 10000, def: 10000]
          media_session_calback_fgs_allowlist_duration_ms: [cur: 10000, def: 10000]
          media_session_callback_fgs_while_in_use_temp_allow_duration_ms: [cur: 10000, def: 10000]"""

        expected = """ownerPid=31847, ownerUid=10461, userId=0
package=com.beatport.mobile
launchIntent=PendingIntent{6654657: PendingIntentRecord{e6a465d com.beatport.mobile startActivity (allowlist: 8019200:+30s0ms/0/NOTIFICATION_SERVICE/NotificationManagerService)}}
mediaButtonReceiver=MBR {pi=null, componentName=ComponentInfo{com.beatport.mobile/com.beatport.mobile.features.streaming.util.CustomMediaReceiver}, type=1, pkg=com.beatport.mobile}
active=true
flags=7
rating type=0
controllers: 5
state=PlaybackState {state=PLAYING(3), position=2910, buffered position=87275, speed=1.0, updated=671962059, actions=7340031, custom actions=[], active item id=0, error=null}
audioAttrs=AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_MUSIC flags=0x800 tags= bundle=null
volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
metadata: size=24, description=We Can Feel It (Original Mix), Dominik Marz, Radial Gaze, Duro
queueTitle=null, size=3"""

        self.assertEqual(extract_first_package_block(output), expected)
