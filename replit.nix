{ pkgs }: {
  deps = [
    pkgs.virtualenv
    pkgs.python311Packages.virtualenv
  ];
  env = {
  };
}