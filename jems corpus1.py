class Parser():
    PREFIXES = ['na', 'nu','ni','ak']
    SUFFIXES = ['khan', 'bo','se','nai','ke']
    MINUMUM_STEM_LENGTH = 3

    @classmethod
    def prefixes(cls, word, internal=False):
        stem = word
        prefix = None
        for potential_prefix in cls.PREFIXES:
            if word.startswith(potential_prefix):
                prefix = potential_prefix
                stem = word[len(prefix):]
                if len(stem) >= cls.MINUMUM_STEM_LENGTH:
                    break
                else:
                    prefix = None
                    stem = word
        if prefix:
            others, stem = cls.prefixes(stem, True)
            others.append(prefix)
            return (others, stem) if internal else (reversed(others), stem)
        else:
            return [], stem

    @classmethod
    def suffixes(cls, word):
        suffix = None
        stem = word
        for potential_suffix in cls.SUFFIXES:
            if word.endswith(potential_suffix):
                suffix = potential_suffix
                stem = word[:-len(suffix)]
                if len(stem) >= cls.MINUMUM_STEM_LENGTH:
                    break
                else:
                    suffix = None
                    stem = word
        if suffix:
            others, stem = cls.suffixes(stem)
            others.append(suffix)
            return others, stem
        else:
            return [], stem

    @classmethod
    def parse(cls, word):
        prefixes, word = cls.prefixes(word)
        suffixes, word = cls.suffixes(word)
        return(tuple(prefixes), word, tuple(suffixes))

words = ['nakhai', 'manukhan', 'khabo', 'marise', 'nakhabe', 'chiryakhan', 'motakhan', 'khaise','nukhulibo','nukuribo','nipindebo','maikekhan','ekdin','purake','moromke','sapake']

parser = Parser()
for word in words:
    print(parser.parse(word))
