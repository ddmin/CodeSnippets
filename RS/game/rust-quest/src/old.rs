use std::fmt;
use std::io::{stdin, stdout, Write};

use rand::Rng;

fn read(input: &mut String) {
    stdout().flush()
        .expect("faled to flush");
    stdin().read_line(input)
        .expect("failed to read");
}

fn dialogue_stop() {
    let mut nothing = String::new();
    print!("== Press Enter to Continue ==");
    read(&mut nothing);
}

fn clear_screen() {
    print!("{}[2J", 27 as char);
}

#[derive(Debug)]
enum Class {
    Warrior,
    Mage,
    Rogue,
    Cleric,
}

enum BattleResult {
   Win(u32),
   Lose,
}

impl BattleResult {
    fn read_result(&self, player: &Player) {
        match self {
            BattleResult::Win(x) => println!("{1} Wins! {1} gained {0} experience.", x, player.name),
            BattleResult::Lose => println!("You Lose!"),
        }
    }
}

// Player Class
#[derive(Debug)]
struct Player {
    name: String,
    level: u32,
    class: Class,
    health: i32,
    attack: i32,
    defense: i32,
    moves: Vec<(String, i32)>,
    exp: u32,
}

impl Player {
    fn new(name: String, class: Class) -> Player{
        let atk = rand::thread_rng().gen_range(5, 16);
        let def = 20 - atk;
        Player {
            name,
            level: 1,
            class,
            health: 500,
            attack: atk,
            defense: def,
            moves: vec![
                ("Punch".to_string(), 10),
                ("Kick".to_string(), 10),
            ],
            exp: 0,
        }
    }

    fn take_damage(&mut self, damage: i32) {
        self.health -= damage;
    }

    fn battle(&mut self, mut monster: Monster) -> BattleResult{
        println!("== The battle begins! ==");
        println!("{} v.s {}\n", self.name, monster.name);
        dialogue_stop();

        // Battle Loop
        let mut turn = 0;
        while self.health >= 0 && monster.health >= 0 {

            // player turn
            clear_screen();
            println!("Combatants:");
            println!("  {}", self);
            println!("  {}\n", monster);

            if turn == 0 {
                println!("== {}'s Turn ==", self.name);

                let mut c = 1;
                println!("{}'s Attacks", self.name);
                for attack in &self.moves {
                    println!("  {}. {:?}", c, attack);
                    c += 1;
                }

                let mut choice = String::new();
                println!();
                println!("Choose an attack");
                print!("> ");
                read(&mut choice);

                let mut attack_num: usize = match choice.trim().parse() {
                    Ok(s) => s,
                    Err(_) => 1,
                };

                if attack_num == 0 {
                    attack_num = 1;
                }

                if attack_num > self.moves.len() {
                    attack_num = 1;
                }

                attack_num -= 1;

                let rng = rand::thread_rng().gen_range(-3, 4);
                let mut dmg = self.moves[attack_num].1 + self.attack;
                dmg = dmg - monster.defense + rng;

                if dmg < 0 {
                    dmg = 0;
                }

                monster.health -= dmg;

                println!();
                println!("{} used {}",
                    self.name,
                    self.moves[attack_num].0,
                );
                println!("It did {} damage.", dmg);
                println!();

            }

            // monster turn
            else if turn == 1 {
                println!("== {}'s Turn ==", monster.name);
                let mmove = rand::thread_rng().gen_range(0, monster.moves.len());
                let mmove = &monster.moves[mmove];

                let rng = rand::thread_rng().gen_range(-3, 4);
                let mut dmg = mmove.1 + monster.attack;
                dmg = dmg - self.defense + rng;

                if dmg < 0 {
                    dmg = 0;
                }

                self.health -= dmg;

                println!("{} used {}.", monster.name, mmove.0);
                println!("It did {} damage.", dmg);
                println!();
            }

            turn = 1 - turn;

            dialogue_stop();

        }

        clear_screen();
        // Player Win
        if monster.health <= 0 {
            println!("{} wins!", self.name);
            dialogue_stop();

            let mut xp: u32 = 0;
            if monster.level > self.level {
                xp = (monster.level - self.level) * 20;
            }

            else {
                xp = monster.level * 10;
            }

            return BattleResult::Win(xp);
        }

        // Enemy Win
        else {
            println!("{} wins!", monster.name);
            dialogue_stop();

            return BattleResult::Lose;
        }
    }
}

impl fmt::Display for Player {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // find class
        let class = match self.class {
            Class::Warrior => "Warrior",
            Class::Mage => "Mage",
            Class::Rogue => "Rogue",
            Class::Cleric => "Cleric",
        };

        write!(f, "[{}] {} -", class, self.name)
            .expect("error");

        write!(f, " (LVL: {},", self.level)
            .expect("error");
        write!(f, " HP: {},", self.health)
            .expect("error");
        write!(f, " ATK: {},", self.attack)
            .expect("error");
        write!(f, " DEF: {})", self.defense)
    }
}


// Monster Class
#[derive(Debug)]
struct Monster {
    name: String,
    class: String,
    level: u32,
    health: i32,
    attack: i32,
    defense: i32,
    moves: Vec<(String, i32)>,
}

impl Monster {
    fn new(name: String, class: String, level: u32, health: i32, attack: i32, defense: i32, moves: Vec<(String, i32)>) -> Monster {
        Monster {
            name,
            class,
            level,
            health,
            attack,
            defense,
            moves,
        }
    }

    fn take_damage(&mut self, damage: i32) {
        self.health -= damage;
    }
}

impl fmt::Display for Monster {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}] {} (LVL: {}, HP: {}, ATK: {}, DEF: {})", self.class, self.name, self.level, self.health, self.attack, self.defense)
    }
}

fn main() {
    let mut player_name = String::new();
    clear_screen();
    println!("What is your name, adventurer?");
    print!("> ");
    read(&mut player_name);
    let player_name = player_name.trim();

    clear_screen();
    println!("Greeting, {}.\n", player_name);
    println!("Choose your class:");

    println!("  1. Warrior");
    println!("  2. Mage");
    println!("  3. Rogue");
    println!("  4. Cleric");

    print!("> ");
    let mut n = String::new();
    read(&mut n);

    let class = match n.chars().next().unwrap() {
        '1' => Class::Warrior,
        '2' => Class::Mage,
        '3' => Class::Rogue,
        '4' => Class::Cleric,
        _ => Class::Warrior,
    };

    let mut player = Player::new(player_name.to_string(), class);

    clear_screen();

    let low_hound = Monster::new(
        "Low Hound".to_string(),
        "Beast".to_string(),
        1,
        10,
        3,
        2,
        vec![("Bite".to_string(), 8)]);

    let high_elf = Monster::new(
        "High Elf".to_string(),
        "Humanoid".to_string(),
        1,
        1000,
        100,
        100,
        vec![("Stomp".to_string(), 10)]);

    // TODO: Add story here

    // Battle
    let result = player.battle(low_hound);
    clear_screen();
    result.read_result(&player);
    dialogue_stop();

    clear_screen();

    // Battle
    let result = player.battle(high_elf);
    clear_screen();
    result.read_result(&player);
    dialogue_stop();
}
