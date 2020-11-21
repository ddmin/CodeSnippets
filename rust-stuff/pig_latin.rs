fn pig_latin(s: &String) -> String {
    let mut c = s.chars();
    let n = match c.next() {
        Some(i) => i,
        None => ' ',
    };
    match n {
        'a' | 'e' | 'i' | 'o' | 'u' => format!("{}-hay", s),
        _ => format!("{}-{}ay", &s[1..], n),
    }
}

fn main() {
    let phrase1 = String::from("apple");
    let phrase2 = String::from("first");
    let phrase3 = String::from("ugway");

    let result1 = pig_latin(&phrase1);
    let result2 = pig_latin(&phrase2);
    let result3 = pig_latin(&phrase3);

    println!("{} -> {}", phrase1, result1);
    println!("{} -> {}", phrase2, result2);
    println!("{} -> {}", phrase3, result3);
}
