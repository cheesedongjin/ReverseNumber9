# ReverseNumber9 Codebase Technical Summary

## Overview
ReverseNumber9 is a static, client-side web application that records audio in the browser, renders a waveform-style visualization while recording, and enables playback and download of both the original and reversed audio. Everything runs in the user’s browser with no server-side components.

## Document Structure (static/index.html)
- **Metadata & Assets**: Loads Google Analytics (`gtag.js`), sets OG tags, uses `icon.png`, and links `style.css` for styling.
- **Navigation**: A simple navbar links to `other-sites/addresses`.
- **Main UI**: A centered container with:
  - Header titles.
  - Recording card containing status indicator, timer, audio visualizer (`canvas`), recording controls, play controls for original/reversed audio, and download links.
- **Script Section**: Defines the `AudioRecorderApp` class encapsulating all functionality.

### `AudioRecorderApp` Responsibilities
- **Initialization**: Caches DOM elements, attaches listeners, and sizes the waveform canvas.
- **Recording Control**:
  - `startRecording()`: Requests microphone access, sets up `AudioContext` with `AnalyserNode` for frequency visualization, configures `MediaRecorder` event handlers to collect chunks, and begins the visualization loop (`drawWaveform`). Updates UI state, timer, and button styles.
  - `stopRecording()`: Stops `MediaRecorder` and associated tracks, closes the audio context, halts the timer, and restores UI state.
- **Visualization**: `drawWaveform()` pulls frequency data from the analyser and draws gradient bars with shadow effects on the canvas; scheduled via `requestAnimationFrame`. Canvas resizes with window events.
- **Post-Processing**: `processRecording()` enables play/download controls, sets the original download blob URL, and generates a reversed audio blob via `createReversedBlob()`.
- **Playback**:
  - `playOriginal()`: Plays the recorded `Blob` with a standard `Audio` element and updates status text on completion.
  - `playReversed()`: Invokes `playBlobReversed()` to decode, reverse channel data, and play through an `AudioBufferSourceNode`, with completion callbacks.
  - `stopCurrentAudio()`: Stops any in-progress playback (supports `pause()` or `stop()`).
- **Audio Reversal & Export**:
  - `audioBufferToWav()`: Serializes an `AudioBuffer` to a WAV `Blob` by manually writing RIFF headers and PCM samples with little-endian formatting.
  - `createReversedBlob()`: Decodes audio data from a `Blob`, reverses each channel’s samples, and returns a new WAV `Blob` using `audioBufferToWav`.
- **UI Feedback**: Status dot colors/styles, timer display, waveform messages, and button enablement respond to recording and playback states.

## Styling (static/style.css)
- **Theme**: Western-inspired palette with tan/brown gradients, wood-grain overlays, and drop shadows; uses the `'Rye'` cursive font.
- **Layout**: Centered container with responsive adjustments; decorative navbar and card framing with nested borders.
- **Controls**: Buttons styled with gradient fills, shadows, hover shine effects, and disabled states. Download links share the thematic styling.
- **Indicators**: Pulsing recording dot animations, timer styling with monospace font, and gradient waveform background for the visualizer area.
- **Responsiveness**: Media query tweaks headers and padding for narrow viewports.

## Ancillary Pages
- **static/404.html**: Minimal 404 page sharing GA and CSS; links back to home.
- **static/other-sites/addresses.html**: Redirects instantly to an external site (`CheeseV`), includes GA and parent styles.
- **static/sitemap.xml**: Declares site URLs for the main page, redirect page, and 404 page.

## Assets
- `static/icon.png`: Favicon referenced by the main page.

## Deployment Context
- Designed for static hosting (e.g., GitHub Pages) with all functionality handled client-side via Web APIs (`MediaRecorder`, `getUserMedia`, Web Audio API, `CanvasRenderingContext2D`).
