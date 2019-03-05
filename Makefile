
analyze:
	./run_analyzer.sh ...

format:
	bazel run --direct_run //:buildifier && \
    find src -type f \( -name '*.m' -o -name '*.mm' -o -name '*cpp' -o -name '*.h' -o -name '*.hpp' \) | \
		xargs -n 1 clang-format --verbose -i --style Google
