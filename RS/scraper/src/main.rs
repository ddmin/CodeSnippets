use std::collections::HashMap;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let query = "apple";
    let link = format!("https://en.wikipedia.org/wiki/{}", query);
    println!("{}", link);
    let resp = reqwest::get(link).await?.text().await?;
    println!("{:#?}", resp);
    Ok(())
}
