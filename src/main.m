#import <Cocoa/Cocoa.h>

int main(int argc, const char *argv[]) {
  // divisin by zero, should be caught by clang-analysis
  __unused int i = 1 / 0;
  return NSApplicationMain(argc, argv);
}
