use rpg::{Class, Game, Hero, Stats};

fn main() {
    let billy = Hero::new("Billy".to_string(), Class::Warrior);
    println!("{}", billy);
}
