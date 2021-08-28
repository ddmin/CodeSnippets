fn christmas_song(arr: &[String]) {
    for i in 1..13 {
        println!("Christmas Day {}:", i);
        for n in (0..i).rev() {
            println!("  {}", arr[n]);
        }
        println!();
    }
}

fn main() {
    let christmas = [
        String::from("1 Partridge in a pear tree"),
        String::from("2 turtle doves"),
        String::from("3 French hens"),
        String::from("4 calling birds"),
        String::from("5 gold rings"),
        String::from("6 geese a-laying"),
        String::from("7 swans a-swimming"),
        String::from("8 maids a-milking"),
        String::from("9 ladies dancing"),
        String::from("10 lords a-leaping"),
        String::from("11 pipers piping"),
        String::from("12 drummers drumming")
    ];

    println!();
    println!("12 Days of Christmas\n");
    christmas_song(&christmas);
}
