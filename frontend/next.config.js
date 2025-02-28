/** @type {import('next').NextConfig} */
const nextConfig = {
  output: "export", // 🔥 This replaces "next export"
  reactStrictMode: true,
  images: {
    unoptimized: true, // Required for AWS Amplify if using images
  },
};

module.exports = nextConfig;