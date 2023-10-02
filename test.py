import lib as l

BRANDS = {
    "ralphlauren": 88
}

if __name__ == "__main__":
    items = l.search("https://www.vinted.it/catalog", {
        # "search_text": "board games",
        "brand_ids[]": BRANDS["ralphlauren"],
        "catalog[]": 5 # men > all
    })

    # Example of filtering
    # [i for i in items if "bimbo" not in i.title or "bambino" not in i.title]

    print(items[0])