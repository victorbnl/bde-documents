{ pkgs, ... }:

{
  languages.python = {
    enable = true;
    uv.enable = true;
  };

  scripts."build".exec = "uv run python src/build.py";
}