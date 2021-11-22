pub enum PartOfSpeech {
    Noun(NounFunction),
    Verb,
    Modifier,
    Ignore,
}

pub enum NounFunction {
    Entity,
    Food,
    Location,
    Time,
    Weapon,
}

pub struct Word {
    pos: PartOfSpeech,
    word: String,
}

impl Word {
    fn new(word: String) -> Word {
        let pos = PartOfSpeech::Ignore;
        Word { pos, word }
    }
}

pub struct Sentence {
    sentence: Vec<Word>,
}

impl Sentence {
    fn new(string: String) -> Sentence {
        todo!()
    }
}

#[cfg(test)]
mod tests {
    use super::*;
}
