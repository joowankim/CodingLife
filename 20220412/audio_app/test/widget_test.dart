import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:audio_app/main.dart';

void main() {
  testWidgets('tab play and stop button', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());

    expect(find.byIcon(Icons.play_arrow), findsOneWidget);
    expect(find.byIcon(Icons.stop), findsNothing);

    await tester.tap(find.byIcon(Icons.play_arrow));
    await tester.pump();

    expect(find.byIcon(Icons.play_arrow), findsNothing);
    expect(find.byIcon(Icons.stop), findsOneWidget);
  });

  testWidgets('tab stop button', (WidgetTester tester) async {
    await tester.pumpWidget(const MyApp());

    await tester.tap(find.byIcon(Icons.play_arrow));
    await tester.pump();

    expect(find.byIcon(Icons.stop), findsOneWidget);
    expect(find.byIcon(Icons.play_arrow), findsNothing);

    await tester.tap(find.byIcon(Icons.stop));
    await tester.pump();

    expect(find.byIcon(Icons.stop), findsNothing);
    expect(find.byIcon(Icons.play_arrow), findsOneWidget);
  });
}
