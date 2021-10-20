use super::hero::Hero;

pub enum GameState {
    Playing,
    GameOver,
}

pub struct Game {
    player: Hero,
    state: GameState,

}

impl Game {
    pub fn new() -> Game {
        todo!();
    }
}

