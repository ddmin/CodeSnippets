use std::fmt;
use std::io::{stdin, stdout, Write};
use rand::Rng;

mod character;
mod screen;
mod ability;

use screen::{read, pause, clear};
use character::{Character, HeroClass, MonsterClass};

use ability::Ability;
use ability::AbilityClass;

fn main() {
    let mut name = String::new();

    println!("What is your name, hero?");
    print!("> ");
    read(&mut name);
    println!();
    name = name.trim().to_string();

    println!("Greetings {}.", name);
    println!();
    println!("Choose your class:");

    println!("  1. Mage");
    println!("  2. Priest");
    println!("  3. Rogue");
    println!("  4. Warrior");

    print!("> ");
    let mut class = String::new();
    read(&mut class);

    let class = match class.chars().next().unwrap() {
        '1' => HeroClass::Mage,
        '2' => HeroClass::Priest,
        '3' => HeroClass::Rogue,
        '4' => HeroClass::Warrior,
        _ => HeroClass::Warrior,
    };

    let mut player = Character::hero(name, class);

    let mut grunt = Character::monster(
        "Robotik Grunt".to_string(),
        [1, 10],
        MonsterClass::Artificial,
        vec![
            Ability::new("Charge".to_string(), AbilityClass::Heal, 5),
            Ability::new("Gear Grind".to_string(), AbilityClass::Attack, 10),
        ]
    );

    let mut boss = Character::monster(
        "Fungus Giant".to_string(),
        [1000, 1001],
        MonsterClass::Flora,
        vec![
            Ability::new("Spores".to_string(), AbilityClass::Attack, 150),
            Ability::new("Attack Growth".to_string(), AbilityClass::Buff(0), 5),
            Ability::new("Cellulize".to_string(), AbilityClass::Buff(1), 5),
            Ability::new("Photosynthesize".to_string(), AbilityClass::Heal, 15),
        ],
    );

    println!("{} <{}>", player, player.stats());
    println!("{}", player.abilities());

    println!();

    println!("{} <{}>", grunt, grunt.stats());
    println!("{}", grunt.abilities());

    println!();

    println!("{} <{}>", boss, boss.stats());
    println!("{}", boss.abilities());
}
