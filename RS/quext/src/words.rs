pub enum PartOfSpeech {
    Noun,
    Verb,
    Modifier,
    Ignore,
}

pub struct Word {
    pos: PartOfSpeech,
    word: String,
}

pub struct Sentence {
    sentence: Vec<PartOfSpeech>,
}

impl Sentence {
    fn new(string: String) -> Sentence {
        string.split_whitespace();
        todo!()
    }
}
