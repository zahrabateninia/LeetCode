// Input: date = "2019-02-10"
// Output: 41

function dayOfYear(date: string): number {
  const year = parseInt(date.slice(0, 4), 10);
  const month = parseInt(date.slice(5, 7), 10);
  const day = parseInt(date.slice(8, 10), 10);

  const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

  const isLeap = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0;

  let total = day;
  for (let i = 0; i < month - 1; i++) {
    total += daysInMonth[i];
  }

  if (isLeap && month > 2) total += 1;

  return total;
}
