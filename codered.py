<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ARCHIVE #0828 — The Day That Never Happened</title>
    <link rel="stylesheet" href="style.css">
</head>

<body>

    <!-- CRT Overlay -->
    <div class="scanlines"></div>
    <div class="noise"></div>

    <!-- Intro -->
    <section id="intro" class="screen active">
        <div class="terminal">
            <p class="tiny">MEMORY RECOVERY SYSTEM v2.8.4</p>

            <h1>ARCHIVE <span>#0828</span></h1>

            <div class="status">
                <span class="dot"></span>
                STATUS: <strong>UNRECOVERED</strong>
            </div>

            <div class="divider"></div>

            <p class="typewriter">
                We found fragments of someone's perfect day.
            </p>

            <p class="subtext">
                The original memory is corrupted.<br>
                Six fragments remain.
            </p>

            <button id="beginBtn">BEGIN RECONSTRUCTION</button>

            <p class="warning">
                ⚠ MEMORY INTEGRITY: 17%
            </p>
        </div>
    </section>


    <!-- Archive -->
    <main id="archive" class="screen">

        <header class="archive-header">
            <div>
                <span class="tiny">MEMORY RECOVERY SYSTEM</span>
                <h2>ARCHIVE #0828</h2>
            </div>

            <div class="archive-status">
                FRAGMENTS FOUND:
                <span id="progress">0 / 6</span>
            </div>
        </header>

        <div class="intro-message">
            <p>Somewhere in this archive is a day that may never have happened.</p>
            <span>Recover the fragments.</span>
        </div>


        <section class="fragments">

            <!-- Photo -->
            <button class="fragment locked" data-fragment="photo">
                <span class="fragment-icon">📸</span>
                <span class="fragment-number">FRAGMENT 01</span>
                <strong>PHOTOGRAPH</strong>
                <small>IMG_0828.DAT</small>
                <span class="recover">CLICK TO RECOVER</span>
            </button>

            <!-- Song -->
            <button class="fragment locked" data-fragment="song">
                <span class="fragment-icon">🎵</span>
                <span class="fragment-number">FRAGMENT 02</span>
                <strong>SONG</strong>
                <small>AUDIO_17.MP3</small>
                <span class="recover">CLICK TO RECOVER</span>
            </button>

            <!-- Message -->
            <button class="fragment locked" data-fragment="message">
                <span class="fragment-icon">💬</span>
                <span class="fragment-number">FRAGMENT 03</span>
                <strong>TEXT MESSAGE</strong>
                <small>MSG_0828.TXT</small>
                <span class="recover">CLICK TO RECOVER</span>
            </button>

            <!-- Sunset -->
            <button class="fragment locked" data-fragment="sunset">
                <span class="fragment-icon">🌅</span>
                <span class="fragment-number">FRAGMENT 04</span>
                <strong>SUNSET</strong>
                <small>IMG_1947.UNKNOWN</small>
                <span class="recover">CLICK TO RECOVER</span>
            </button>

            <!-- Ticket -->
            <button class="fragment locked" data-fragment="ticket">
                <span class="fragment-icon">🎟️</span>
                <span class="fragment-number">FRAGMENT 05</span>
                <strong>TICKET</strong>
                <small>EVENT_0828.PDF</small>
                <span class="recover">CLICK TO RECOVER</span>
            </button>

            <!-- Note -->
            <button class="fragment locked" data-fragment="note">
                <span class="fragment-icon">📝</span>
                <span class="fragment-number">FRAGMENT 06</span>
                <strong>HANDWRITTEN NOTE</strong>
                <small>NOTE_FINAL.JPG</small>
                <span class="recover">CLICK TO RECOVER</span>
            </button>

        </section>

        <div class="archive-footer">
            <span>RECOVERY PROGRESS</span>
            <div class="progress-bar">
                <div id="progressFill"></div>
            </div>
        </div>

    </main>


    <!-- Modal -->
    <div id="modal" class="modal">

        <div class="modal-box">

            <button id="closeModal" class="close">×</button>

            <div id="modalContent"></div>

            <button id="nextBtn" class="next-btn">
                RETURN TO ARCHIVE
            </button>

        </div>

    </div>


    <!-- Final -->
    <section id="ending" class="screen ending">

        <div class="ending-content">

            <span class="tiny">ARCHIVE #0828 — RECONSTRUCTION COMPLETE</span>

            <div class="ending-icon">✓</div>

            <h1>You reconstructed<br>the day.</h1>

            <p class="pause">But there's one problem...</p>

            <h2>Nobody remembers living it.</h2>

            <div class="glitch-line"></div>

            <p class="final-note">
                Archive status has changed.
            </p>

            <p class="status-error">
                STATUS: <span>IMPOSSIBLE</span>
            </p>

            <button id="restartBtn">REOPEN ARCHIVE</button>

        </div>

    </section>


    <script src="script.js"></script>
</body>
</html>

style.css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=Space+Mono:wght@400;700&display=swap');

:root {
    --bg: #080b0a;
    --panel: #0d1210;
    --green: #8aff9c;
    --green-dark: #285c35;
    --text: #d7e6da;
    --muted: #68776c;
    --red: #ff5f5f;
    --yellow: #d8c875;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    background: var(--bg);
    color: var(--text);
    font-family: "IBM Plex Mono", monospace;
    min-height: 100vh;
    overflow-x: hidden;
}


/* CRT EFFECT */

.scanlines {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 999;
    opacity: 0.08;

    background: repeating-linear-gradient(
        to bottom,
        transparent 0px,
        transparent 3px,
        #ffffff 4px
    );
}

.noise {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 998;
    opacity: 0.035;

    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.8'/%3E%3C/svg%3E");
}


/* GENERAL */

.screen {
    min-height: 100vh;
    display: none;
}

.screen.active {
    display: flex;
}


/* INTRO */

#intro {
    align-items: center;
    justify-content: center;
    padding: 30px;
}

.terminal {
    width: min(700px, 100%);
    border: 1px solid #26382b;
    background: rgba(10, 15, 12, 0.94);
    padding: 55px;
    box-shadow:
        0 0 50px rgba(77, 255, 119, 0.04),
        inset 0 0 80px rgba(0, 0, 0, 0.5);

    position: relative;
}

.terminal::before {
    content: "●  ●  ●";
    position: absolute;
    top: 13px;
    left: 18px;
    color: #39483d;
    letter-spacing: 4px;
    font-size: 10px;
}

.tiny {
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 2px;
}

.terminal h1 {
    margin-top: 30px;
    font-size: clamp(42px, 8vw, 78px);
    line-height: 0.95;
    letter-spacing: -4px;
    color: var(--green);
    text-shadow: 0 0 15px rgba(138, 255, 156, 0.25);
}

.terminal h1 span {
    display: block;
    color: #718075;
    font-size: 0.55em;
    letter-spacing: 2px;
    margin-top: 10px;
}

.status {
    margin-top: 28px;
    color: #84968a;
    font-size: 13px;
}

.status strong {
    color: var(--red);
}

.dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    background: var(--red);
    border-radius: 50%;
    margin-right: 8px;
    box-shadow: 0 0 10px var(--red);
}

.divider {
    height: 1px;
    background: #253429;
    margin: 30px 0;
}

.typewriter {
    color: white;
    font-size: 18px;
    line-height: 1.8;
}

.subtext {
    color: #718075;
    margin-top: 15px;
    line-height: 1.8;
    font-size: 13px;
}

button {
    font-family: inherit;
}

#beginBtn,
#restartBtn {
    margin-top: 35px;
    background: transparent;
    border: 1px solid var(--green-dark);
    color: var(--green);
    padding: 14px 20px;
    cursor: pointer;
    letter-spacing: 1px;
    transition: 0.25s;
}

#beginBtn:hover,
#restartBtn:hover {
    background: var(--green);
    color: #061008;
    box-shadow: 0 0 25px rgba(138, 255, 156, 0.15);
}

.warning {
    margin-top: 30px;
    color: #505c53;
    font-size: 10px;
}


/* ARCHIVE */

#archive {
    display: none;
    flex-direction: column;
    padding: 35px;
    max-width: 1250px;
    margin: auto;
}

#archive.active {
    display: flex;
}

.archive-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 1px solid #26382b;
    padding-bottom: 20px;
}

.archive-header h2 {
    color: var(--green);
    font-size: 25px;
    margin-top: 8px;
}

.archive-status {
    color: var(--muted);
    font-size: 11px;
}

#progress {
    color: var(--green);
    margin-left: 8px;
}

.intro-message {
    padding: 50px 10px 35px;
}

.intro-message p {
    font-size: clamp(18px, 3vw, 27px);
    color: #dce9de;
}

.intro-message span {
    display: block;
    color: var(--muted);
    margin-top: 12px;
    font-size: 12px;
}


/* FRAGMENTS */

.fragments {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
}

.fragment {
    min-height: 220px;
    background: linear-gradient(145deg, #0d1410, #080d0a);
    border: 1px solid #26382b;
    color: var(--text);
    padding: 25px;
    text-align: left;
    cursor: pointer;
    position: relative;

    display: flex;
    flex-direction: column;

    transition:
        transform 0.3s,
        border-color 0.3s,
        background 0.3s;
}

.fragment:hover {
    transform: translateY(-4px);
    border-color: var(--green-dark);
    background: #101a13;
}

.fragment-icon {
    font-size: 32px;
    filter: grayscale(1);
    opacity: 0.75;
    margin-bottom: 25px;
}

.fragment-number {
    color: var(--muted);
    font-size: 9px;
    letter-spacing: 2px;
}

.fragment strong {
    color: var(--green);
    font-size: 15px;
    margin-top: 7px;
}

.fragment small {
    color: #4e5b52;
    margin-top: 7px;
}

.recover {
    margin-top: auto;
    font-size: 9px;
    color: #5b6d60;
    letter-spacing: 1px;
}

.fragment.recovered {
    border-color: #406849;
}

.fragment.recovered .fragment-icon {
    filter: grayscale(0);
    opacity: 1;
}

.fragment.recovered .recover {
    color: var(--green);
}


/* PROGRESS */

.archive-footer {
    margin-top: 35px;
    font-size: 9px;
    color: var(--muted);
}

.progress-bar {
    height: 4px;
    background: #182219;
    margin-top: 10px;
}

#progressFill {
    height: 100%;
    width: 0%;
    background: var(--green);
    box-shadow: 0 0 10px rgba(138, 255, 156, 0.3);
    transition: width 0.5s;
}


/* MODAL */

.modal {
    position: fixed;
    inset: 0;
    background: rgba(2, 5, 3, 0.88);
    backdrop-filter: blur(8px);

    display: none;
    align-items: center;
    justify-content: center;

    z-index: 100;
    padding: 20px;
}

.modal.open {
    display: flex;
}

.modal-box {
    width: min(650px, 100%);
    max-height: 90vh;
    overflow-y: auto;

    background: #0c120e;
    border: 1px solid #38543e;
    padding: 40px;

    box-shadow:
        0 0 80px rgba(0, 0, 0, 0.8),
        0 0 20px rgba(138, 255, 156, 0.04);

    position: relative;
}

.close {
    position: absolute;
    top: 12px;
    right: 15px;
    background: none;
    border: none;
    color: #647268;
    font-size: 25px;
    cursor: pointer;
}

.close:hover {
    color: white;
}

.fragment-title {
    color: var(--green);
    font-size: 11px;
    letter-spacing: 2px;
}

.fragment-heading {
    font-size: 30px;
    margin-top: 10px;
    margin-bottom: 25px;
}

.modal-text {
    color: #9ca99f;
    line-height: 1.9;
    font-size: 14px;
}

.memory-card {
    border: 1px dashed #3c5741;
    padding: 25px;
    margin-top: 20px;
    background: #090e0b;
}

.fake-photo {
    height: 230px;
    background:
        linear-gradient(
            to top,
            #101812 0%,
            #263f2d 40%,
            #6c805d 58%,
            #d1aa70 59%,
            #19231a 61%,
            #080c09 100%
        );
    position: relative;
    overflow: hidden;
    margin-bottom: 20px;
}

.fake-photo::after {
    content: "";
    position: absolute;
    width: 100px;
    height: 150px;
    background: #070907;
    left: 50%;
    bottom: -50px;
    transform: translateX(-50%);
    border-radius: 50% 50% 0 0;
}

.audio-player {
    border: 1px solid #304534;
    padding: 20px;
    margin-top: 20px;
}

.audio-line {
    height: 2px;
    background: #2c3d30;
    position: relative;
    margin: 20px 0;
}

.audio-line::after {
    content: "";
    position: absolute;
    width: 35%;
    height: 100%;
    background: var(--green);
}

.lyrics {
    color: #a7b8aa;
    font-style: italic;
    line-height: 2;
}

.chat {
    margin-top: 20px;
}

.chat-message {
    padding: 12px 15px;
    background: #172119;
    margin: 8px 0;
    max-width: 80%;
    font-size: 13px;
}

.chat-message.right {
    margin-left: auto;
    background: #223329;
    color: var(--green);
}

.ticket {
    border: 1px dashed #7c7350;
    background: #18170f;
    color: #ded29b;
    padding: 25px;
    margin-top: 20px;
}

.ticket-title {
    font-size: 22px;
    margin-bottom: 20px;
}

.note {
    background: #d5caa2;
    color: #25251d;
    padding: 35px 25px;
    margin-top: 20px;
    font-family: Georgia, serif;
    transform: rotate(-1deg);
    box-shadow: 4px 6px 15px rgba(0, 0, 0, 0.4);
}

.note p {
    font-size: 19px;
    line-height: 1.8;
}

.next-btn {
    margin-top: 30px;
    border: 1px solid #334b38;
    background: transparent;
    color: var(--green);
    padding: 12px 18px;
    cursor: pointer;
}

.next-btn:hover {
    background: var(--green);
    color: #071008;
}


/* ENDING */

#ending {
    display: none;
}

#ending.active {
    display: flex;
}

.ending {
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 30px;
}

.ending-content {
    max-width: 800px;
}

.ending-icon {
    width: 55px;
    height: 55px;
    border: 1px solid var(--green);
    color: var(--green);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 40px auto 25px;
    font-size: 25px;
}

.ending h1 {
    color: var(--green);
    font-size: clamp(38px, 7vw, 75px);
    line-height: 1;
    letter-spacing: -3px;
}

.pause {
    margin-top: 60px;
    color: #667269;
    font-size: 14px;
}

.ending h2 {
    margin-top: 25px;
    color: white;
    font-size: clamp(22px, 4vw, 38px);
}

.glitch-line {
    width: 200px;
    height: 1px;
    background: var(--red);
    margin: 40px auto;
    box-shadow: 40px 0 #56755d, -50px 0 #725b5b;
}

.final-note {
    color: #59665d;
    font-size: 11px;
}

.status-error {
    margin-top: 10px;
    color: #7d8880;
    font-size: 11px;
}

.status-error span {
    color: var(--red);
}


/* ANIMATIONS */

@keyframes flicker {
    0%, 19%, 21%, 63%, 64%, 100% {
        opacity: 1;
    }

    20%, 62% {
        opacity: 0.65;
    }
}

@keyframes glitch {
    0% {
        transform: translate(0);
    }

    20% {
        transform: translate(-2px, 1px);
    }

    40% {
        transform: translate(2px, -1px);
    }

    60% {
        transform: translate(-1px, 2px);
    }

    80% {
        transform: translate(1px, -2px);
    }

    100% {
        transform: translate(0);
    }
}

.ending h1 {
    animation: flicker 4s infinite;
}


/* RESPONSIVE */

@media (max-width: 800px) {

    .terminal {
        padding: 35px 25px;
    }

    .archive-header {
        align-items: flex-start;
        gap: 20px;
        flex-direction: column;
    }

    .fragments {
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 550px) {

    #archive {
        padding: 20px;
    }

    .fragments {
        grid-template-columns: 1fr;
    }

    .fragment {
        min-height: 180px;
    }

    .modal-box {
        padding: 30px 20px;
    }
}

script.js
const beginBtn = document.getElementById("beginBtn");
const archive = document.getElementById("archive");
const intro = document.getElementById("intro");

const modal = document.getElementById("modal");
const modalContent = document.getElementById("modalContent");
const closeModal = document.getElementById("closeModal");
const nextBtn = document.getElementById("nextBtn");

const ending = document.getElementById("ending");
const restartBtn = document.getElementById("restartBtn");

const progressText = document.getElementById("progress");
const progressFill = document.getElementById("progressFill");

const fragments = document.querySelectorAll(".fragment");

let recovered = new Set();


// Fragment content
const memories = {

    photo: `
        <span class="fragment-title">FRAGMENT 01 / IMAGE RECOVERY</span>

        <h2 class="fragment-heading">The Photograph</h2>

        <div class="fake-photo"></div>

        <div class="memory-card">
            <p class="modal-text">
                A photograph recovered from an unknown camera.
                <br><br>
                Two people are standing beside a lake.
                Neither face is recognizable.
                <br><br>
                Timestamp:
                <strong>08:28 AM</strong>
                <br><br>
                The strange part?
                The photograph contains a shadow belonging to a third person.
            </p>
        </div>
    `,

    song: `
        <span class="fragment-title">FRAGMENT 02 / AUDIO RECOVERY</span>

        <h2 class="fragment-heading">The Song</h2>

        <div class="audio-player">

            <p class="modal-text">
                UNKNOWN TRACK — 03:47
            </p>

            <div class="audio-line"></div>

            <p class="lyrics">
                "If tomorrow forgets today,<br>
                meet me where the sunlight fades..."
            </p>

        </div>

        <div class="memory-card">
            <p class="modal-text">
                Metadata indicates the song was played at
                <strong>11:42 AM</strong>.
                <br><br>
                No copy of this song exists anywhere in the archive.
            </p>
        </div>
    `,

    message: `
        <span class="fragment-title">FRAGMENT 03 / COMMUNICATION RECOVERY</span>

        <h2 class="fragment-heading">The Text Message</h2>

        <div class="chat">

            <div class="chat-message">
                You awake?
            </div>

            <div class="chat-message right">
                I'm outside.
            </div>

            <div class="chat-message">
                Outside where?
            </div>

            <div class="chat-message right">
                Your favorite place.
            </div>

            <div class="chat-message">
                I don't have a favorite place.
            </div>

            <div class="chat-message right">
                You will today.
            </div>

        </div>

        <div class="memory-card">
            <p class="modal-text">
                Message timestamp:
                <strong>01:13 PM</strong>
                <br><br>
                Recipient: UNKNOWN
            </p>
        </div>
    `,

    sunset: `
        <span class="fragment-title">FRAGMENT 04 / VISUAL RECOVERY</span>

        <h2 class="fragment-heading">The Sunset</h2>

        <div class="fake-photo" style="
            background:
            linear-gradient(
                to bottom,
                #141927,
                #734c55 45%,
                #db8a61 62%,
                #302218 63%,
                #070a08 100%
            );
        "></div>

        <div class="memory-card">
            <p class="modal-text">
                Location data corrupted.
                <br><br>
                Timestamp:
                <strong>07:47 PM</strong>
                <br><br>
                Someone wrote in the metadata:
                <br><br>
                <em>"This is exactly how I wanted the sky to look."</em>
            </p>
        </div>
    `,

    ticket: `
        <span class="fragment-title">FRAGMENT 05 / PHYSICAL RECOVERY</span>

        <h2 class="fragment-heading">The Ticket</h2>

        <div class="ticket">

            <div class="ticket-title">
                ONE DAY ONLY
            </div>

            <p>
                EVENT: THE PERFECT EVENING
            </p>

            <br>

            <p>
                DATE: 08 / 28
            </p>

            <p>
                TIME: 08:28 PM
            </p>

            <p>
                SEAT: ∞
            </p>

            <br>

            <p>
                ADMIT ONE
            </p>

        </div>

        <div class="memory-card">
            <p class="modal-text">
                Ticket has no venue.
                <br><br>
                No event matching this ticket has ever existed.
            </p>
        </div>
    `,

    note: `
        <span class="fragment-title">FRAGMENT 06 / FINAL RECOVERY</span>

        <h2 class="fragment-heading">The Handwritten Note</h2>

        <div class="note">

            <p>
                If you're reading this,
                then you found all of it.
            </p>

            <br>

            <p>
                The coffee.<br>
                The music.<br>
                The lake.<br>
                The sunset.
            </p>

            <br>

            <p>
                Everything happened exactly
                the way we wanted.
            </p>

            <br>

            <p>
                Please don't try to remember me.
            </p>

            <br>

            <p>
                — You
            </p>

        </div>
    `
};


// BEGIN
beginBtn.addEventListener("click", () => {

    intro.classList.remove("active");

    setTimeout(() => {
        archive.classList.add("active");
    }, 400);

});


// OPEN FRAGMENT
fragments.forEach(fragment => {

    fragment.addEventListener("click", () => {

        const type = fragment.dataset.fragment;

        openFragment(type);

    });

});


function openFragment(type) {

    modalContent.innerHTML = memories[type];

    modal.classList.add("open");

    // Mark as recovered
    if (!recovered.has(type)) {

        recovered.add(type);

        const fragment = document.querySelector(
            `[data-fragment="${type}"]`
        );

        fragment.classList.remove("locked");
        fragment.classList.add("recovered");

        updateProgress();
    }

}


// UPDATE PROGRESS
function updateProgress() {

    const count = recovered.size;

    progressText.textContent = `${count} / 6`;

    const percentage = (count / 6) * 100;

    progressFill.style.width = `${percentage}%`;


    // All memories recovered
    if (count === 6) {

        nextBtn.textContent = "COMPLETE RECONSTRUCTION";

    }

}


// CLOSE
function closeMemory() {

    modal.classList.remove("open");

    if (recovered.size === 6) {

        nextBtn.textContent = "ENTER FINAL ARCHIVE";

    }

}


closeModal.addEventListener("click", closeMemory);


// NEXT
nextBtn.addEventListener("click", () => {

    modal.classList.remove("open");

    if (recovered.size === 6) {

        setTimeout(() => {

            archive.classList.remove("active");
            ending.classList.add("active");

        }, 600);

    }

});


// Click outside modal
modal.addEventListener("click", (event) => {

    if (event.target === modal) {
        closeMemory();
    }

});


// ESC closes modal
document.addEventListener("keydown", (event) => {

    if (event.key === "Escape") {
        modal.classList.remove("open");
    }

});


// RESTART
restartBtn.addEventListener("click", () => {

    recovered.clear();

    fragments.forEach(fragment => {
        fragment.classList.remove("recovered");
        fragment.classList.add("locked");
    });

    updateProgress();

    ending.classList.remove("active");

    setTimeout(() => {
        intro.classList.add("active");
    }, 300);
