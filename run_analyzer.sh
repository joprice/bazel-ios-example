# based on https://github.com/cybrown-zoox/bazel-clang-analyzer

set -eux

BAZEL_TARGET=$1
TITLE="Clang analyzer report for Bazel Target $1"
REPO_ROOT=$PWD
EXECUTION_ROOT=`bazel info execution_root`

bazel clean
bazel build --experimental_action_listener=tools/actions:generate_compile_commands_listener ...
python3 tools/actions/generate_compile_commands_json.py

export SDKROOT=`xcrun --sdk macosx --show-sdk-path`
export DEVELOPER_DIR=`xcode-select -p`

cd $EXECUTION_ROOT

# running custom version until bazel integration is fixed
#python3 $HOME/dev/github.com/rizsotto/scan-build/run.py \
analyze-build \
    --cdb $REPO_ROOT/compile_commands.json \
    -o $REPO_ROOT/clang-analysis \
    --html-title "$TITLE" \
    --use-analyzer external/local_config_cc/wrapped_clang \
    -v
# use these with above fork
#--use-cc=external/local_config_cc/wrapped_clang \
#--use-c++=external/local_config_cc/wrapped_clang \

cd -
