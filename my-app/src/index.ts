import 'source-map-support/register';

// 3p
import { Config, createApp, displayServerURL } from '@foal/core';

// App
import { AppController } from './app/app.controller';
import { dataSource } from './db';
import HuggingFace from 'huggingface';

// HuggingFace
import { pipeline } from '@xenova/transformers';

async function main() {
  await dataSource.initialize();

  const app = await createApp(AppController);
  const myHeaders = new Headers();
  myHeaders.append("Accept", "application/json");

  const requestOptions: RequestInit = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
  };

  fetch("https://www.dnd5eapi.co/api/monsters/adult-black-dragon", requestOptions)
    .then(response => response.text())
    .then(result => console.log(JSON.stringify(JSON.parse(result))))
    .catch(error => console.log('error', error));
  console.log();
  
  const pipe = await pipeline("sentiment-analysis");
  const out = await pipe('I love transformers!');
  console.log(out);

  const port = Config.get('port', 'number', 3001);
  app.listen(port, () => displayServerURL(port));
}

main()
  .catch(err => { console.error(err.stack); process.exit(1); })

