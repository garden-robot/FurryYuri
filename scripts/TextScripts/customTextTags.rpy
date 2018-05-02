#Custom Text Tags

#Tag for when Eve whispers
init python:
    def eveSmall_tag(tag, arguments, contents):
        return [
                (renpy.TEXT_TAG, u"size=-10"),
            ] + contents + [
                (renpy.TEXT_TAG, u"/size"),
            ]
    config.custom_text_tags["eveSmall"] = eveSmall_tag