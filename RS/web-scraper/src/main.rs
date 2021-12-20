use scraper::*;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let query = "apple";
    let link = format!("https://en.wikipedia.org/wiki/{}", query);

    let response = reqwest::get(&link).await?.text().await?;

    let parsed_html = Html::parse_document(&response);

    let div_selector = Selector::parse("div.mw-parser-output").unwrap();
    let p_selector = Selector::parse("p").unwrap();

    let div = parsed_html.select(&div_selector).next().unwrap();
    let ps = div.select(&p_selector).collect::<Vec<_>>();

    for element in ps {
        println!("{:?}", element.text().collect::<Vec<_>>());
    }

    Ok(())
}
