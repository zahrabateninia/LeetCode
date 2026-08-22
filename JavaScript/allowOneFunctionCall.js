function once(fn) {
  let hasBeenCalled = false;
  let result;

  return (...args) => {
    if (!hasBeenCalled) {
      result = fn(...args);
      hasBeenCalled = true;
      return result;
    } else {
      return undefined;
    }
  };
}