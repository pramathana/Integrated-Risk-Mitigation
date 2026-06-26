const fs = require('fs');
const readline = require('readline');

const transcriptPath = "C:\\Users\\Jesano Pramathana\\.gemini\\antigravity-ide\\brain\\e0f03029-3d01-47ef-8456-b64840f9596d\\.system_generated\\logs\\transcript_full.jsonl";

async function extractOriginalData() {
  const fileStream = fs.createReadStream(transcriptPath);
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  let bestMatch = "";

  for await (const line of rl) {
    if (line.includes('const evaluationData = [')) {
      const parsed = JSON.parse(line);
      const content = parsed.content || '';
      
      // Look for the version that has the detailed T.02 text
      if (content.includes('IT Security Risk at PT. Citilink Indonesia:')) {
          const startIndex = content.indexOf('const evaluationData = [');
          if (startIndex !== -1) {
              const substring = content.substring(startIndex, startIndex + 15000);
              bestMatch = substring;
          }
      }
    }
  }
  
  if (bestMatch) {
      fs.writeFileSync('evalDataTarget.txt', bestMatch);
      console.log('Saved best match to evalDataTarget.txt');
  } else {
      console.log('Not found');
  }
}
extractOriginalData();
