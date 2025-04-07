const uuidv4 = () => {
  return '10000000-1000-4000-8000-100000000000'.replace(/[018]/g, (c) =>
    (
      +c ^
      (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (+c / 4)))
    ).toString(16)
  );
};

const callButton = document.getElementById('callButton');
const cancelButton = document.getElementById('cancelButton');
const ws = new WebSocket('ws://localhost:8000/ws');
const callerId = uuidv4();

let isCalling;
let audioChunks;
let sendInterval;
let chunkCounter = 0;

let audioContext;
let stream;
let source;
let processor;
let sampleRate;

ws.onopen = () => {
  console.log('WebSocket connected');
  isCalling = true;
};

cancelButton.onclick = () => {
  isCalling = false;
  if (sendInterval) {
    clearInterval(sendInterval);
    sendInterval = null;
  }

  processor.disconnect();
  source.disconnect();
  audioContext.close();

  callButton.disabled = false;
  cancelButton.disabled = true;
  stream.getTracks().forEach((track) => track.stop());
};

ws.onclose = () => {
  console.log('WebSocket disconnected');
  if (isCalling) {
    cancelButton.onclick();
  }
};

ws.onerror = (error) => {
  console.error('WebSocket error:', error);
};

callButton.addEventListener('click', async () => {
  callButton.disabled = true;
  cancelButton.disabled = false;
  audioChunks = [];
  sendInterval = null;
  chunkCounter = 0;

  audioContext = new AudioContext();
  stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  source = audioContext.createMediaStreamSource(stream);
  processor = audioContext.createScriptProcessor(16384, 1, 1);
  sampleRate = audioContext.sampleRate;

  source.connect(processor);
  processor.connect(audioContext.destination);

  processor.onaudioprocess = (e) => {
    if (!isCalling) return;

    const inputData = e.inputBuffer.getChannelData(0);
    audioChunks.push(new Float32Array(inputData));
    if (!sendInterval) {
      sendInterval = setInterval(() => {
        if (audioChunks.length > 0 && ws.readyState === WebSocket.OPEN) {
          let combinedLength = audioChunks.reduce(
            (acc, chunk) => acc + chunk.length,
            0
          );
          let combinedAudio = new Float32Array(combinedLength);

          let position = 0;
          for (const chunk of audioChunks) {
            combinedAudio.set(chunk, position);
            position += chunk.length;
          }

          // Split into two parts
          const halfLength = Math.floor(combinedAudio.length / 2);
          const firstHalf = combinedAudio.slice(0, halfLength);
          const secondHalf = combinedAudio.slice(halfLength);

          // Send first part
          const firstData = {
            id: callerId,
            type: 'TRANSCRIBE',
            sample_rate: sampleRate,
            audio: Array.from(firstHalf),
            model: {
                name: 'WHISPER',
                size: 'large-v3',
            }
          };
          ws.send(JSON.stringify(firstData));
          console.log(`Sent audio chunk part 1, size: ${firstHalf.length}`);

          // Send second part after a short delay
          setTimeout(() => {
            const secondData = {
              id: callerId,
              type: 'TRANSCRIBE',
              sample_rate: sampleRate,
              audio: Array.from(secondHalf),
              model: {
                  name: 'WHISPER',
                  size: 'large-v3',
              }
            };
            ws.send(JSON.stringify(secondData));
            console.log(`Sent audio chunk part 2, size: ${secondHalf.length}`);
          }, 500); // 500ms between the two sends

          // Reset chunks
          audioChunks = [];
          chunkCounter += 2;
        }
      }, 5000); // Changed from 1000ms to 2000ms (2 seconds)
    }
  };
});

const output = document.getElementById('output');

ws.onmessage = (event) => {
  try {
    const data = JSON.parse(event.data);

    if (data.type === 'TRANSCRIBE' && data.text) {
      const transcription = document.createElement('p');
      transcription.textContent = data.text;

      const timestamp = new Date().toLocaleTimeString();
      transcription.innerHTML = `<strong>[${timestamp}]</strong> ${data.text}`;

      output.appendChild(transcription);

      output.scrollTop = output.scrollHeight;
    }
  } catch (error) {
    console.error('Error processing message:', error);
  }
};