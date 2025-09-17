import unittest

from parse_dumpsys import parse_data, parse_metadata, get_object_fields, remove_redundant_comas


class TestParseDumpsys(unittest.TestCase):

    def setUp(self):
        self.youtube_music_sample = """YouTube playerlib com.google.android.apps.youtube.music/YouTube playerlib (userId=0)
      ownerPid=30676, ownerUid=10239, userId=0
      package=com.google.android.apps.youtube.music
      launchIntent=PendingIntent{b094326: PendingIntentRecord{2ec1c26 com.google.android.apps.youtube.music startActivity}}
      mediaButtonReceiver=MBR {pi=PendingIntent{2390681: PendingIntentRecord{abf9368 com.google.android.apps.youtube.music broadcastIntent}}, componentName=ComponentInfo{com.google.android.apps.youtube.music/androidx.media.session.MediaButtonReceiver}, type=1, pkg=com.google.android.apps.youtube.music}
      active=true
      flags=3
      rating type=2
      controllers: 5
      state=PlaybackState {state=PLAYING(3), position=0, buffered position=0, speed=1.0, updated=556998420, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232770, mExtras=null, Action:mName='Like, mIcon=2131233493, mExtras=null, Action:mName='Repeat off, mIcon=2131232683, mExtras=null, Action:mName='Dislike, mIcon=2131233486, mExtras=null], active item id=51, error=null}
      audioAttrs=AudioAttributes: usage=USAGE_MEDIA content=CONTENT_TYPE_UNKNOWN flags=0x800 tags= bundle=null
      volumeType=LOCAL, controlType=ABSOLUTE, max=0, current=0, volumeControlId=null
      metadata: size=7, description=Aqualung (Steven Wilson Stereo Remix), Jethro Tull, Jethro Tull
      queueTitle=Up next, size=25"""

    def test_parse_dumpsys_contains(self):
        result = parse_data(self.youtube_music_sample)

        self.assertIsInstance(result, dict)
        self.assertEqual(result["package"], "com.google.android.apps.youtube.music")
        self.assertEqual(result["active"], "true")
        self.assertTrue(result["state"].startswith("PlaybackState {state=PLAYING"))
        self.assertIn("metadata", result)
        self.assertIn("queueTitle", result)

    def test_parse_dumpsys_equals(self):
        self.assertEqual(parse_data("ownerPid=27953, ownerUid=10239, userId=0"),
                         {"ownerPid": "27953", "ownerUid": "10239", "userId": "0"})

        self.assertEqual(parse_data("active=true"),
                         {"active": "true"})

        self.assertEqual(parse_data("flags=3"),
                         {"flags": "3"})

        self.assertEqual(parse_data("queueTitle=Up next, size=25"),
                         {"queueTitle": "Up next", "size": "25"})

        self.assertEqual(
            parse_data("metadata: size=9, description=…con lentitud poderosa, Chris Christodoulou, Risk of Rain 2"),
            {"metadata": "size=9, description=…con lentitud poderosa, Chris Christodoulou, Risk of Rain 2"})

        self.assertEqual(
            parse_data(
                "launchIntent=PendingIntent{ceba381: PendingIntentRecord{2ec1c26 com.google.android.apps.youtube.music startActivity}}"),
            {
                "launchIntent": "PendingIntent{ceba381: PendingIntentRecord{2ec1c26 com.google.android.apps.youtube.music startActivity}}"})

        self.assertEqual(
            parse_data(
                "state=PlaybackState {state=PLAYING(3), position=0, buffered position=0, speed=1.0, updated=556998420, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232770, mExtras=null, Action:mName='Like, mIcon=2131233493, mExtras=null, Action:mName='Repeat off, mIcon=2131232683, mExtras=null, Action:mName='Dislike, mIcon=2131233486, mExtras=null], active item id=51, error=null}"),
            {
                "state": "PlaybackState {state=PLAYING(3), position=0, buffered position=0, speed=1.0, updated=556998420, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232770, mExtras=null, Action:mName='Like, mIcon=2131233493, mExtras=null, Action:mName='Repeat off, mIcon=2131232683, mExtras=null, Action:mName='Dislike, mIcon=2131233486, mExtras=null], active item id=51, error=null}"})

        self.assertEqual(
            parse_data(
                "state=PLAYING(3), position=0, buffered position=0, speed=1.0, updated=556998420, actions=2600887, custom actions=[Action:mName='Shuffle off, mIcon=2131232770, mExtras=null, Action:mName='Like, mIcon=2131233493, mExtras=null, Action:mName='Repeat off, mIcon=2131232683, mExtras=null, Action:mName='Dislike, mIcon=2131233486, mExtras=null], active item id=51, error=null"),
            {
                "state": "PLAYING(3)",
                "position": "0",
                "buffered position": "0",
                "speed": "1.0",
                "updated": "556998420",
                "actions": "2600887",
                "custom actions": "[Action:mName='Shuffle off, mIcon=2131232770, mExtras=null, Action:mName='Like, mIcon=2131233493, mExtras=null, Action:mName='Repeat off, mIcon=2131232683, mExtras=null, Action:mName='Dislike, mIcon=2131233486, mExtras=null]",
                "active item id": "51",
                "error": "null"})

        self.assertEqual(parse_data(""), {})

    def test_parse_metadata_simple(self):
        metadata = "metadata: size=7, description=Bourée , Jethro Tull  , Stand Up"
        track = parse_metadata(metadata)
        self.assertEqual(track.title, "Bourée")
        self.assertEqual(track.artist, "Jethro Tull")

    def test_parse_metadata_king_complicated(self):
        metadata = 'metadata: size=7, description=21st Century Schizoid Man (Including "Mirrors"), King Crimson, In the Court of the Crimson King'
        track = parse_metadata(metadata)
        self.assertEqual(track.title, '21st Century Schizoid Man (Including "Mirrors")')
        self.assertEqual(track.artist, "King Crimson")

    def test_parse_metadata_missing_description(self):
        metadata = "metadata: size=7"
        self.assertRaises(IndexError, lambda: parse_metadata(metadata))

    def test_get_object_fields_basic(self):
        obj = "{state=PLAYING, position=0}"
        self.assertEqual(get_object_fields(obj), "state=PLAYING, position=0")

    def test_get_object_fields_multiple_braces(self):
        obj = "outer{inner={key=value}}outer_end"
        self.assertEqual(get_object_fields(obj), "inner={key=value}")

    def test_get_object_fields_no_braces(self):
        obj = "no braces here"
        self.assertEqual(get_object_fields(obj), obj)

    def test_get_object_fields_one_braces(self):
        obj = "Object {no braces here"
        self.assertEqual(get_object_fields(obj), obj)

    def test_remove_redundant_comas(self):
        self.assertEqual(remove_redundant_comas(",a,b,"), "a,b")
        self.assertEqual(remove_redundant_comas("a,b"), "a,b")
        self.assertEqual(remove_redundant_comas(",a,b"), "a,b")
        self.assertEqual(remove_redundant_comas("a,b,"), "a,b")
