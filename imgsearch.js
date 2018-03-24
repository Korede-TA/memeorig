const puppeteer = require('puppeteer');

const TEST_URL = "https://pbs.twimg.com/media/DXpdVIFVwAA0Bsx.jpg";
const API_KEY = "AIzaSyBWaY98vwnvaBGvRxCCMH8YNOpUOcFtcaM";
const CX = "004140975131308375580:oghwufu6das";
const RESULT_COUNT = 10;
const QUERY = "%s 'pbs.twimg.com/media/' inurl:twitter.com inurl:status";
const BASE = "https://www.googleapis.com/customsearch/v1?q=%s&key=%s&cx=%s&image_url=%s)";

function imagesearch(url=TEST_URL) {
	const browser = await puppeteer.launch();
	const page = await browser.newPage();

	let reqUrl = "https://www.googleapis.com/customsearch/v1?q=${QUERY}&key=${API_KEY}&cx=${CX}&image_url=${url})";
	await page.goto(reqUrl);
	await page.screenshot({path: 'example.png'});

	await browser.close();
}

