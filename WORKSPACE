load("@bazel_tools//tools/build_defs/repo:git.bzl", "git_repository")

git_repository(
    name = "build_bazel_rules_apple",
    # using unreleased fix for mac provision profile file suffix
    commit = "d020ed9e950d5d38b32a26fee232292cd7176d58",
    remote = "https://github.com/bazelbuild/rules_apple.git",
)

load(
    "@build_bazel_rules_apple//apple:repositories.bzl",
    "apple_rules_dependencies",
)

apple_rules_dependencies()

load(
    "@build_bazel_apple_support//lib:repositories.bzl",
    "apple_support_dependencies",
)

apple_support_dependencies()

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "six_archive",
    build_file = "six.BUILD",
    url = "https://pypi.python.org/packages/source/s/six/six-1.10.0.tar.gz",
)

#
bind(
    name = "six",
    actual = "@six_archive//:six",
)

# buildifier is written in Go and hence needs rules_go to be built.
# See https://github.com/bazelbuild/rules_go for the up to date setup instructions.
#http_archive(
#    name = "io_bazel_rules_go",
#    sha256 = "f87fa87475ea107b3c69196f39c82b7bbf58fe27c62a338684c20ca17d1d8613",
#    url = "https://github.com/bazelbuild/rules_go/releases/download/0.16.2/rules_go-0.16.2.tar.gz",
#)
http_archive(
    name = "io_bazel_rules_go",
    sha256 = "7994c62f36aa67c961fa2972e7961a68095d3c29c7d3bc631500a220a042de39",
    url = "https://github.com/bazelbuild/rules_go/releases/download/0.16.7/rules_go-0.16.7.tar.gz",
)

load("@io_bazel_rules_go//go:def.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains()

http_archive(
    name = "com_github_bazelbuild_buildtools",
    strip_prefix = "buildtools-55b64c3d2ddfb57f06477c1d94ef477419c96bd6",
    url = "https://github.com/bazelbuild/buildtools/archive/55b64c3d2ddfb57f06477c1d94ef477419c96bd6.zip",
)

load("@com_github_bazelbuild_buildtools//buildifier:deps.bzl", "buildifier_dependencies")

buildifier_dependencies()
