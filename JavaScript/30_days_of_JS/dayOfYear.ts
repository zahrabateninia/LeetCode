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


// Leap year rule: 
// a year is a leap year if it’s divisible by 4,
// except for century years, which must also be divisible by 400. 
// This matters here because the range includes 1900 (not a leap year, since it’s divisible by 100 but not 400)
// and 2000 (a leap year, since it’s divisible by 400).

// Why month > 2: 
// the extra leap day (Feb 29) only counts if the date falls after
// February. For a date in February itself, day already covers it.

// Parsing:
// since the format is guaranteed, slicing by fixed positions
// is cleaner than split('-') and avoids allocating an intermediate array.