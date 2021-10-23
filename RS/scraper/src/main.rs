use roux;
use roux::util::{FeedOption, TimePeriod};
use std::fs;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    // const USER_AGENT: &str = "linux:rust (by /u/alterproncount)";

    // let contents = fs::read_to_string("secrets.conf").expect("Could not read file.");
    // let contents = contents.split_whitespace();

    // let contents: Vec<_> = contents.collect();
    // let username = contents[0];
    // let password = contents[1];
    // let client_secret = contents[2];
    // let client_id = contents[3];

    // let client = roux::Reddit::new(USER_AGENT, client_id, client_secret)
    //     .username(username)
    //     .password(password)
    //     .login()
    //     .await;

    // let me = client.unwrap();
    // let upvoted = me.upvoted().await.unwrap().data;

    let subreddit = roux::Subreddit::new("astolfo");

    // Gets top 10 posts from this month
    let options = FeedOption::new().period(TimePeriod::ThisMonth);
    let top = subreddit.top(25, Some(options)).await;
    println!("{:?}", top);

    Ok(())
}
