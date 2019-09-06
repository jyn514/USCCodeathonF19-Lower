SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p in
mkdir -p out

pushd $SCRIPT_DIR

  for i in {1..10}
  do
    python3 ./mkin.py >> in/in$i;
    python3 ./solutions/solution.py < in/in$i >> out/out$i
  done

  for i in "example1" "example2" "in11"
  do
    python3 ./solutions/solution.py < in/$i >> out/$i
  done

  mv out/in11 out/out11
popd
