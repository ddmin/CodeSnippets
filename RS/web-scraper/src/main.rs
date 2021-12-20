use scraper::*;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let query = "apple";
    let link = format!("https://en.wikipedia.org/wiki/{}", query);

    let response = reqwest::get(&link).await?.text().await?;

    let parsed = Html::parse_document(&response);

    println!("{:?}", parsed);
    println!("LINK: {}", link);

    Ok(())
}
