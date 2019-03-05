load("@com_github_bazelbuild_buildtools//buildifier:def.bzl", "buildifier")

buildifier(
    name = "buildifier",
)

load("@build_bazel_rules_apple//apple:versioning.bzl", "apple_bundle_version")
load("@build_bazel_rules_apple//apple:macos.bzl", "macos_application", "macos_unit_test")

objc_library(
    name = "lib",
    srcs = glob(["src/*.m"]),
    hdrs = glob(["src/*.h"]),
)

apple_bundle_version(
    name = "version",
    build_version = "0.0.1",
    short_version_string = "0.1",
)

macos_application(
    name = "app",
    #app_icons = glob(["resources/mac.xcassets/**/*"]),
    bundle_id = "com.joprice.example",
    entitlements = "resources/entitlements.plist",
    infoplists = ["resources/Info.plist"],
    linkopts = [
        "-framework Security",
    ],
    minimum_os_version = "10.10",
    #provisioning_profile = "//provision_profiles:production",
    version = ":version",
    deps = [":lib"],
)
