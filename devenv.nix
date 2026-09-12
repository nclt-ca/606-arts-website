{ pkgs, ... }:

{
  packages = with pkgs; [
    hugo
    nodejs_22
  ];

  languages.javascript = {
    enable = true;
    package = pkgs.nodejs_22;
  };

  scripts.dev.exec = ''
    hugo server --bind 127.0.0.1
  '';

  scripts.build.exec = ''
    hugo --minify
  '';

  scripts.format.exec = ''
    npm run format
  '';

  enterShell = ''
    echo "🏗️  606 Art Space - Local Development Environment"
    echo ""
    echo "Available commands:"
    echo "  dev     - Start Hugo development server"
    echo "  build   - Build the site for production"
    echo "  format  - Format code with Prettier"
    echo ""
    hugo version
    echo "Node $(node --version)"
  '';
}
