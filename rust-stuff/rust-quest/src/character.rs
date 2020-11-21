use std::fmt;
use rand::Rng;

use crate::ability::Ability;
use crate::ability::AbilityClass;

// TODO: Items

// Base Health is 200 HP, scales 10 HP per level
// Base Stat is 20 points, scales 1 per level

// Generate character stats
fn generate_stats(level: u32) -> (i32, i32, i32, i32) {
    let level = level as i32;
    let health = 200 + 10 * (level - 1);
    let speed = rand::thread_rng().gen_range(1, 4 + level / 4);

    let stat_points = 20 + 1 * (level - 1) - speed;

    let attack = rand::thread_rng().gen_range(5, stat_points);
    let defense = stat_points - attack;

    // (HP, ATK, DEF, SPD)
    (health, attack, defense, speed)
}

pub enum HeroClass {
    Mage,
    Priest,
    Rogue,
    Warrior,
}

impl fmt::Display for HeroClass {
    // Display trait for HeroClass
    fn fmt(&self, f:&mut fmt::Formatter) -> fmt::Result {

        let class = match self {
            HeroClass::Mage => "Mage".to_string(),
            HeroClass::Priest => "Priest".to_string(),
            HeroClass::Rogue => "Rogue".to_string(),
            HeroClass::Warrior => "Warrior".to_string(),
        };

        write!(f, "{}", class)
    }
}

pub enum MonsterClass {
    Arcane,
    Artificial,
    Beast,
    Flora,
    Humanoid,
}

impl fmt::Display for MonsterClass {
    // Display trait for monster_type
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {

        let class = match self {
            MonsterClass::Arcane => "Arcane".to_string(),
            MonsterClass::Artificial => "Artificial".to_string(),
            MonsterClass::Beast => "Beast".to_string(),
            MonsterClass::Flora => "Flora".to_string(),
            MonsterClass::Humanoid => "Humanoid".to_string(),
        };

        write!(f, "{}", class)
    }
}

pub struct Character<T> {
    pub name: String,
    pub level: u32,
    pub class: T,
    pub health: i32,
    pub attack: i32,
    pub defense: i32,
    pub speed: i32,
    pub abilities: Vec<Ability>,
}

impl<T> Character<T> where T: fmt::Display {
     // initialize hero
    pub fn hero(name: String, class: T) -> Character<T> {

        let (hp, atk, def, spd) = generate_stats(1);

        let ability = Ability::new("Punch".to_string(), AbilityClass::Attack, 10);

        Character {
            name: name,
            level: 1,
            class: class,
            health: hp,
            attack: atk,
            defense: def,
            speed: spd,
            abilities: vec![ability],
        }
    }

    // initialize monster
    pub fn monster(
        name: String,
        levels: [u32; 2],
        class: T,
        abilities: Vec<Ability>) -> Character<T> {

        let level = rand::thread_rng().gen_range(levels[0], levels[1]);
        let (hp, atk, def, spd) = generate_stats(level);

        Character {
            name: name,
            level: level,
            class: class,
            health: hp,
            attack: atk,
            defense: def,
            speed: spd,
            abilities: abilities,
        }
    }

    // display stats
    pub fn stats(&self) -> String {
        format!("HP: {} | ATK: {} | DEF: {} | SPD: {}",
                self.health, self.attack, self.defense, self.speed)
    }

    pub fn abilities(&self) -> String {
        let mut abilities = String::new();
        let mut n = 1;

        for ability in &self.abilities {
            abilities += &format!("  {}. {}", n, ability);
            if n != self.abilities.len() {
                abilities += "\n";
            }
            n += 1;
        }

        abilities
    }
 }

impl<T> fmt::Display for Character<T> where T: fmt::Display {
    // Display trait for Player
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}] {} (Lv {})", self.class, self.name, self.level)
    }
}
