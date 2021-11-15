use roux::Subreddit;
use tokio;

#[tokio::main]
async fn main() {
    let subreddit = Subreddit::new("rust");
    // Now you are able to:

    // Get moderators.
    let moderators = subreddit.moderators().await;

    // Get hot posts with limit = 25.
    let hot = subreddit.hot(25, None).await;

    // Get rising posts with limit = 30.
    let rising = subreddit.rising(30, None).await;

    // Get top posts with limit = 10.
    let top = subreddit.top(10, None).await;

    // Get latest comments.
    // `depth` and `limit` are optional.
    let latest_comments = subreddit.latest_comments(None, Some(25)).await;

    // Get comments from a submission.
    let article_id = &hot.unwrap().data.children.first().unwrap().data.id.clone();
    let article_comments = subreddit.article_comments(article_id, None, Some(25)).await;
    println!("{:#?}", article_comments);
}
